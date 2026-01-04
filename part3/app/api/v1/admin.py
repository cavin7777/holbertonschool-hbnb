from app.services import facade
from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from flask import request

api = Namespace('admin', description='Admin operations')

@api.route('/users/')
class AdminUserCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt()
        if not current_user.get('is_admin', False):
            return {'error': 'Admin privileges required'}, 403

        user_data = request.json
        email = user_data.get('email')

        # Check if email is already in use
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        # Logic to create a new user
        new_user = facade.create_user(user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201

@api.route('/users/<user_id>')
class AdminUserResource(Resource):
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt()
        
        # If 'is_admin' is part of the identity payload
        if not current_user.get('is_admin', False):
            return {'error': 'Admin privileges required'}, 403

        data = request.json
        email = data.get('email')

        if email:
            # Check if email is already in use
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email is already in use'}, 400

        # Logic to update user details, including email and password
        updated_user = facade.update_user(user_id, data)
        return {
            'id': updated_user.id,
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'email': updated_user.email
        }, 200

@api.route('/amenities/')
class AdminAmenityCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt()
        if not current_user.get('is_admin', False):
            return {'error': 'Admin privileges required'}, 403

        # Logic to create a new amenity
        name = request.json.get('name')
        if facade.get_amenity_by_name(name):
            return {'error': 'Amenity already exists'}, 400

        amenity = facade.create_amenity({'name': name})
        return {'id': amenity.id, 'name': amenity.name}, 201

@api.route('/amenities/<amenity_id>')
class AdminAmenityModify(Resource):
    @jwt_required()
    def put(self, amenity_id):
        current_user = get_jwt()
        if not current_user.get('is_admin', False):
            return {'error': 'Admin privileges required'}, 403

        # Logic to update an amenity
        data = request.json
        updated_amenity = facade.update_amenity(amenity_id, data)
        return {'id': updated_amenity.id, 'name': updated_amenity.name}, 200

@api.route('/places/<place_id>')
class AdminPlaceModify(Resource):
    @jwt_required()
    def put(self, place_id):
        current_user = get_jwt()

        # Set is_admin default to False if not exists
        is_admin = current_user.get('is_admin', False)
        user_id = current_user.get('id')

        # Logic to update the place
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404

        if not is_admin and place.owner_id != user_id:
            return {'error': 'Unauthorized action'}, 403
        
        updated_place = facade.update_place(place_id, request.json)
        return {'message': 'Place updated', 'id': updated_place.id}, 200

@api.route('/reviews/<review_id>')
class AdminReviewModify(Resource):
    @jwt_required()
    def put(self, review_id):
        current_user = get_jwt()
        # Set is_admin default to False if not exists
        is_admin = current_user.get('is_admin', False)
        user_id = current_user.get('id')

        # Logic to update the review
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404

        if not is_admin and review.user_id != user_id:
            return {'error': 'Unauthorized action'}, 403

        updated_review = facade.update_review(review_id, request.json)
        return {'message': 'Review updated', 'id': updated_review.id}, 200

    @jwt_required()
    def delete(self, review_id):
        current_user = get_jwt()
        # Set is_admin default to False if not exists
        is_admin = current_user.get('is_admin', False)
        user_id = current_user.get('id')

        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404

        if not is_admin and review.user_id != user_id:
            return {'error': 'Unauthorized action'}, 403

        facade.delete_review(review_id)
        return {'message': 'Review deleted'}, 200