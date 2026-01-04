from .base_model import BaseModel
from .user import User
from .place import Place

class Review(BaseModel):
    def __init__(self, text, rating, place: Place, user: User):
        super().__init__()

        self.text = self.validate_name(text, "text", 500)
        self.rating = rating
        self.place = self.validate_place(place, "place")
        self.user = self.validate_user(user, "user")

        if not isinstance(rating, int) or not 1 <= rating <= 5:
            raise ValueError("Rating must be an integer between 1 and 5")
