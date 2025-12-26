from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'place_id': fields.String(required=True, description='ID of the place'),
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new review"""
        # Placeholder for the logic to register a new review
        current_user_id = get_jwt_identity()
        data = api.payload
        place = facade.get_place(data['place_id'])
        if not place:
            return {'error': 'Place not found'}, 404
        
        # Check user is not the owner
        if place.owner.id == current_user_id:
            return {'error': 'You cannot review your own place.'}, 400
        
        # Check user has not already reviewed this place
        existing_reviews = facade.get_reviews_for_place(data['place_id'])
        if any(r.user.id == current_user_id for r in existing_reviews):
            return {'error': 'You have already reviewed this place.'}, 400

        review = facade.create_review({
            'place': place,
            'user_id': current_user_id,
            'rating': data['rating'],
            'text': data['text']
        })
        return review.to_dict(), 201
    
    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        # Placeholder for logic to return a list of all reviews
        reviews = facade.get_all_reviews()
        return [r.to_dict() for r in reviews], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        # Placeholder for the logic to retrieve a review by ID
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return review.to_dict(), 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, review_id):
        """Update a review's information"""
        # Placeholder for the logic to update a review by ID
        current_user_id = get_jwt_identity()
        review = facade.get_review(review_id)
        
        if not review:
            return {'error': 'Review not found'}, 404

        if review.user.id != current_user_id:
            return {'error': 'Unauthorized action'}, 403

        data = api.payload
        updated_review = facade.update_review(review_id, data)
        return {'message': 'Review updated successfully', 'review': updated_review.to_dict()}, 200

    @api.response(200, 'Review deleted successfully')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        # Placeholder for the logic to delete a review
        current_user_id = get_jwt_identity()
        review = facade.get_review(review_id)

        if not review:
            return {'error': 'Review not found'}, 404

        if review.user.id != current_user_id:
            return {'error': 'Unauthorized action'}, 403

        facade.delete_review(review_id)
        return {'message': 'Review deleted successfully'}, 200