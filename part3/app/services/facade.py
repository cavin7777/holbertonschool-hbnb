import uuid
from app.persistence.repository import InMemoryRepository
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    #PASSWORD FACADE

    def hash_password(self, password):
        return generate_password_hash(password)

    def verify_password(self, password, user: User):
        """Verify password using the User instance."""
        if not user or not user.password:
            return False
        return user.verify_password(password)

    # USER FACADE
    def create_user(self, first_name, last_name, email, password):
        user = User(first_name, last_name, email)
        user.hash_password(password)  # hash password BEFORE storage
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    # AMENITY FACADE
    def create_amenity(self, amenity_data):
        if not amenity_data.get("name"):
            raise ValueError("Amenity name is required")

        amenity = Amenity(name=amenity_data["name"])
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
        if "name" in amenity_data:
            amenity.name = amenity_data["name"]
        self.amenity_repo.update(amenity_id, {"name": amenity.name})
        return amenity

    # PLACE FACADE
    def create_place(self, place_data):
        try:
            owner = self.user_repo.get(place_data['owner_id'])
            if not owner:
                raise ValueError("Owner does not exist")

            amenities = []
            for amenity_id in place_data.get("amenities", []):
                amenity = self.amenity_repo.get(amenity_id)
                if not amenity:
                    raise ValueError(f"Amenity not found: {amenity_id}")
                amenities.append(amenity)

            place_data_copy = place_data.copy()
            place_data_copy.pop("owner_id", None)
            place_data_copy.pop("amenities", None)
            place = Place(owner=owner, **place_data_copy)
            place.amenities = amenities

            self.place_repo.add(place)
            return place

        except Exception as e:
            raise ValueError(str(e))

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        return place

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            return None

        # Allowed updates
        for key, value in place_data.items():
            if key == "owner_id":
                owner = self.user_repo.get(value)
                if not owner:
                    raise ValueError("Owner not found")
                place.owner = owner
            elif key == "amenities":
                new_amenities = []
                for aid in value:
                    amenity = self.amenity_repo.get(aid)
                    if not amenity:
                        raise ValueError(f"Amenity not found: {aid}")
                    new_amenities.append(amenity)
                place.amenities = new_amenities
            else:
                setattr(place, key, value)

        self.place_repo.update(place_id, place)
        return place


    # REVIEW FACADE
    def create_review(self, review_data):
        pass

    def get_review(self, review_id):
        pass

    def get_all_reviews(self):
        pass

    def get_reviews_by_place(self, place_id):
        pass

    def update_review(self, review_id, review_data):
        pass

    def delete_review(self, review_id):
        pass
