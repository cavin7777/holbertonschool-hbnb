from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.services.repositories.user_repository import UserRepository
from app.services.repositories.place_repository import PlaceRepository
from app.services.repositories.review_repository import ReviewRepository
from app.services.repositories.amenity_repository import AmenityRepository
  
class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.place_repo = PlaceRepository()
        self.review_repo = ReviewRepository()
        self.amenity_repo = AmenityRepository()
    
    # -------------------- Placeholder method for USER --------------------
    def create_user(self, user_data):
        user = User(**user_data)
        # user.hash_password(user_data["password"])
        self.user_repo.add(user)
        return user
    
    def get_user(self, user_id):    
        return self.user_repo.get(user_id)

    def get_all_users(self):
        return self.user_repo.get_all()
    
    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)
    
    def update_user(self, user_id, data):
        user = self.get_user(user_id)
        if not user:
            return None
        
        if 'first_name' in data:
            user.first_name_value = data.pop('first_name')

        if 'last_name' in data:
            user.last_name_value = data.pop('last_name')

        self.user_repo.update(user_id, data)
        return user
    
    # # -------------------- Placeholder method for AMENITY --------------------
    def create_amenity(self, amenity_data):
        if "name" not in amenity_data:
            raise ValueError("Amenity name is required")
        
        existing = self.amenity_repo.get_by_attribute("name", amenity_data["name"])
        if existing:
            return existing
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity
    
    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)
    
    def get_all_amenities(self):
        return self.amenity_repo.get_all()
    
    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None
        if "name" in amenity_data:
            amenity.name = amenity.validate_name(
                amenity_data["name"], "name", 50)
        
        self.amenity_repo.update(amenity_id, amenity_data)
        return amenity
    
    # # -------------------- Placeholder method for PLACE --------------------
    def create_place(self, place_data):
        owner = self.get_user(place_data.get('owner_id'))
        if not owner:
            return None
        
        amenities = place_data.pop('amenities', [])
        place = Place(**place_data)
        place.amenities = []
        
        for name in amenities:
            if not name:
                continue
            amenity = self.amenity_repo.get_by_attribute("name", name)
            if not amenity:
                amenity = Amenity(name=name)
                self.amenity_repo.add(amenity)
            place.amenities.append(amenity)      
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if not place:
            return None
        self.place_repo.update(place_id, place_data)
        return place
    
    # # -------------------- Placeholder method for REVIEW --------------------
    def create_review(self, review_data):
    # Placeholder for logic to create a review, including validation for user_id, place_id, and rating
        user = self.get_user(review_data.get('user_id'))
        place = self.get_place(review_data.get('place_id'))
        if not user or not place:
            return None
        
        review = Review(text=review_data.get("text"), rating=review_data.get("rating"), user=user, place=place)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
    # Placeholder for logic to retrieve a review by ID
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
    # Placeholder for logic to retrieve all reviews
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
    # Placeholder for logic to retrieve all reviews for a specific place
        place = self.get_place(place_id)
        if not place:
            return None
        # Get reviews from the repository filtered by place_id
        return [r for r in self.review_repo.get_all() if r.place_id == place_id]

    def update_review(self, review_id, review_data):
    # Placeholder for logic to update a review
        review = self.get_review(review_id)
        if not review:
            return None
        self.review_repo.update(review_id, review_data)
        return review
    
    def user_already_reviewed_place(self, user_id, place_id):
        """
        Returns True if the user has already reviewed the place, False otherwise
        """
        reviews = self.review_repo.get_all()
        for review in reviews:
            if review.user_id == user_id and review.place_id == place_id:
                return True
        return False

    def delete_review(self, review_id):
    # Placeholder for logic to delete a review
        review = self.get_review(review_id)
        if not review:
            return False
        self.review_repo.delete(review_id)
        return True