import uuid
from datetime import datetime
from .user import User

class Place:
    def __init__(self, title, description, price, latitude, longitude, owner, id=None):
        # Validations
        if not title or len(title) > 100:
            raise ValueError("title is required and must be <= 100 characters")
        if price < 0:
            raise ValueError("price must be positive")
        if not (-90 <= latitude <= 90):
            raise ValueError("latitude must be between -90 and 90")
        if not (-180 <= longitude <= 180):
            raise ValueError("longitude must be between -180 and 180")
        if not isinstance(owner, User):
            raise TypeError("owner must be a User instance")

        # Core attributes
        self.id = id or str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner

        # Relationships
        self.reviews = []
        self.amenities = []

        # Link back to owner
        if not hasattr(owner, "places"):
            owner.places = []
        owner.places.append(self)

    def to_dict(self):
        """Full serialization including owner and amenities"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner": self.owner.to_dict() if self.owner else None,
            "amenities": [{"id": a.id, "name": a.name} for a in self.amenities],
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    def to_dict_basic(self):
        """Basic serialization, also JSON serializable"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "owner": self.owner.to_dict() if self.owner else None,
            "amenities": [{"id": a.id, "name": a.name} for a in self.amenities]
        }

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update attributes based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
