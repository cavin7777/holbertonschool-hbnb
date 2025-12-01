import uuid
from datetime import datetime
from .place import Place
from .user import User
class Review:
    def __init__(self, text, rating, place, user):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

        if not text:
            raise ValueError("Review text cannot be empty")

        if not (1 <= rating <= 5):
            raise ValueError("rating must be between 1 and 5")

        if not isinstance(place, Place):
            raise TypeError("place must be a Place instance")

        if not isinstance(user, User):
            raise TypeError("user must be a User instance")

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Update the updated_at timestamp