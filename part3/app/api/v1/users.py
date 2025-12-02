from flask import jsonify, request
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_register_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='User password')
})

user_response_model = api.model("UserResponse", {
    "id": fields.String(description="User ID"),
    "message": fields.String(description="Response message")
})

user_login_model = api.model('Login', {
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})

user_response_model = api.model("UserResponse", {
    "id": fields.String(description="User ID"),
    "first_name": fields.String(),
    "last_name": fields.String(),
    "email": fields.String()
})
@api.route('/')
class UserList(Resource):
    @api.expect(user_register_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        # Hash the password BEFORE saving user
        hashed_password = facade.hash_password(user_data["password"])
        user_data["password"] = hashed_password

        new_user = facade.create_user(**user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201
    
@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200

@api.route('/login')
class UserLogin(Resource):
    @api.expect(api.model('Login', {
        'email': fields.String(required=True),
        'password': fields.String(required=True)
    }))
    @api.response(200, 'Login successful')
    @api.response(400, 'Email and password are required')
    @api.response(401, 'Invalid email or password')
    def post(self):
        """User login"""
        data = api.payload
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return {'message': 'Email and password are required'}, 400

        # Find user by email
        user = facade.get_user_by_email(email)
        if not user or not facade.verify_password(password, user.password):
            return {'message': 'Invalid email or password'}, 401

        return {'message': f'Welcome {user.first_name}!', 'id': user.id}, 200
