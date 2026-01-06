from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the place model fcreation or input validation and documentation
place_create = api.model('PlaceCreate', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

# Define the place model update for input validation and documentation
place_update = api.model('PlaceUpdate', {
    'title': fields.String(description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(description='Price per night'),
})

@api.route('/')
class PlaceList(Resource):
    @jwt_required()
    @api.expect(place_create)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        # Placeholder for the logic to register a new place
        current_user = get_jwt_identity()
        place_data = api.payload
        place_data['owner_id'] = current_user
        new_place = facade.create_place(place_data)

        if not new_place:
            return {'error': 'Owner not found'}, 400
        return {'id': new_place.id, 'title': new_place.title, 'description': new_place.description, 'price': new_place.price, 'latitude': new_place.latitude, 'longitude': new_place.longitude,'owner_id': new_place.owner_id}, 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        # Placeholder for logic to return a list of all places
        places = facade.get_all_places()
        return [{'id': place.id, 'title': place.title, 'description': place.description, 'price': place.price, 'latitude': place.latitude, 'longitude': place.longitude,} for place in places], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        # Placeholder for the logic to retrieve a place by ID, including associated owner and amenities
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        
        response =  {"id": place.id, "title": place.title, "description": place.description, "latitude": place.latitude, "longitude": place.longitude}
        owner = facade.get_user(place.owner_id)
        if owner:
                response["owner"] = {"id": owner.id, "first_name": owner.first_name, "last_name": owner.last_name, "email": owner.email}
            
        response["amenities"] = [{"id": amenity.id, "name": amenity.name} for amenity in place.amenities]
        return response, 200
    
    @jwt_required()
    @api.expect(place_update)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        # Placeholder for the logic to update a place by ID
        current_user = get_jwt_identity()
        place_data = api.payload
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        if place.owner_id != current_user:
            return {'error': 'Unauthorized action'}, 403
        
        updated_place = facade.update_place(place_id, place_data)
        return {"message": "Place updated successfully"}, 200
    
@api.route('/<place_id>/reviews')
class PlaceReviews(Resource):
    @api.response(200, 'List of reviews for a place')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        reviews = facade.get_reviews_by_place(place_id)

        if reviews is None:
            return {'error': 'Place not found'}, 404

        return [
            {
                'id': review.id,
                'text': review.text,
                'rating': review.rating
            }
            for review in reviews
        ], 200