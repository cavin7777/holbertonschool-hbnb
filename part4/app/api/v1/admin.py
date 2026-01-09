from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

api = Namespace('admin', description='Admin operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='User password')
})

user_update_model = api.model('UserUpdate', {
    'first_name': fields.String(required=False, description='First name of the user'),
    'last_name': fields.String(required=False, description='Last name of the user'),
    'email': fields.String(required=False, description='Email of the user'),
    'password': fields.String(required=False, description='User password')
})

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

amenity_update_model = api.model('AmenityUpdate', {
    'name': fields.String(required=False, description='Name of the amenity')
})
@api.route('/users/')
class AdminUserCreate(Resource):
    @api.expect(user_model, validate=True)
    @jwt_required()
    def post(self):
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403 # OK TEST
        
        user_data = api.payload
        email = user_data.get('email')
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400 #OK TEST
        
        # Logic to create a new user
        new_user = facade.create_user(user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201

@api.route('/users/<user_id>')
class AdminUserModify(Resource):
    @api.expect(user_update_model, validate=True)
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403 # OK TEST

        user_data = api.payload
        if not user_data:
            return {'error': 'No data provided'}, 404 # OK TEST
        
        user = facade.get_user(user_id)
        if not user:
            return {'error': "User_ID doesn't exist"}, 404 # OK TEST
        
        email = user_data.get('email')

        if email:
            existing_mail = facade.get_user_by_email(email)
            if existing_mail and existing_mail.id != user_id:
                return {'error': 'Email already registered'}, 400 #OK TEST
        
        try:
            updated_user = facade.update_user(user_id, user_data)
        except ValueError as e:
            return {'error': str(e)}, 400
             
        return {'id': updated_user.id, 'first_name': updated_user.first_name, 'last_name': updated_user.last_name}, 200

@api.route('/amenities/')
class AdminAmenityCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        
        # Logic to create a new amenity
        amenity_data = api.payload
        try:
            new_amenity = facade.create_amenity(amenity_data)
        except ValueError as e:
            return {'error': str(e)}, 400
        return {'id': new_amenity.id, 'name': new_amenity.name}, 201
@api.route('/amenities/<amenity_id>')
class AdminAmenityModify(Resource):
    @jwt_required()
    def put(self, amenity_id):
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        # Logic to update an amenity
        amenity_data = api.payload
        if not amenity_data:
            return {'error': 'No data provided'}, 400

        name = amenity_data.get('name')
        if name is not None:
            # Check if the name is not empty or whitespace
            if not name.strip():
                return {'error': 'Amenity name cannot be empty'}, 400
        
        existing = facade.amenity_repo.get_by_attribute("name", name)
        if existing:
            return {"error": "Amenity name already exists"}, 400

        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': "Amenity not found"}, 404

        try:
            updated_amenity = facade.update_amenity(amenity_id, amenity_data)
        except ValueError as e:
            return {'error': str(e)}, 400

        return {'id': updated_amenity.id, 'name': updated_amenity.name}, 200

@api.route('/places/<place_id>')
class AdminPlaceModify(Resource):
    @jwt_required()
    def put(self, place_id):
        current_user = get_jwt()

        # Set is_admin default to False if not exists
        is_admin = current_user.get('is_admin', False)
        user_id = current_user.get('id')

        place = facade.get_place(place_id)
        if not is_admin and place.owner_id != user_id:
            return {'error': 'Unauthorized action'}, 403

        # Logic to update the place
        pass
