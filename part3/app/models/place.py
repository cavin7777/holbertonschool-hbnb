from app.models.base_model import BaseModel
from app.extensions import db
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship

place_amenity = db.Table(
    'place_amenity', db.Model.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True)
)
class Place(BaseModel):
    __tablename__ = "places"  # Must be class-level, not inside __init__
    # Columns
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
    amenities = db.relationship("Amenity", secondary=place_amenity, back_populates="places")
    reviews = db.relationship("Review", back_populates="place", cascade="all, delete-orphan")

    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=None, reviews=None):
        super().__init__()
        self.title = self.validate_name(title, "title", 100)
        self.description = description
        self.price = self.validate_price(price)     
        self.latitude = self.validate_coordinate(latitude, "latitude", -90, 90)
        self.longitude = self.validate_coordinate(longitude, "longitude", -180, 180)
        self.owner_id = owner_id

    def validate_price(self, price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be positive value")
        return float(price)
    
    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        if amenity not in self.amenities:
            self.amenities.append(amenity)