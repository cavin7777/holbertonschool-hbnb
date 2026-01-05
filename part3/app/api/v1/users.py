from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade
from werkzeug.security import generate_password_hash

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='User password')
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(404, 'Invalid input data')

    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_mail = facade.get_user_by_email(user_data['email'])
        if existing_mail:
            return {'error': 'Email already registered'}, 400

        password = user_data.pop('password')
        user_data['password'] = password
        
        new_user = facade.create_user(user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201

    def get(self):
        """ Retrieve a list of all users """
        users = facade.get_all_users()
        return [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email} for user in users], 200

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User_ID not found')

    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User_ID not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200
    
    @jwt_required()
    @api.expect(user_model)
    @api.response(200, 'User details modified successfully')
    @api.response(400, 'Email and Password cannot be modify')
    @api.response(404, 'Invalid Data')
    def put(self, user_id):
        """ Update user information """
        current_user = get_jwt_identity()
        user_data = api.payload
        user = facade.get_user(user_id)

        if not user:
            return {'error': "User_ID doesn't exist"}, 404
        if user_id != current_user:
            return {'error': 'Unauthorized action'}, 403
        if not user_data:
            return {'error': 'No data provided'}, 404
        
        first_name = user_data.get('first_name')
        last_name = user_data.get('last_name')
        if not first_name or len(first_name) > 50:
            return {'error': 'first_name must filled and be at most 50 characters'}, 404
        if not last_name or len(last_name) > 50:
            return {'error': 'last_name must be filled and be at most 50 characters'}, 404

        if 'email' in user_data or 'password' in user_data:
            return {'error': 'Email and password cannot be modified here'}, 400
                    
        updated_user = facade.update_user(user_id, user_data)
        return {'id': updated_user.id, 'first_name': updated_user.first_name, 'last_name': updated_user.last_name, 'email': updated_user.email}, 200
