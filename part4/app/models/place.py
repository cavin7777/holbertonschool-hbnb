from app.models.base_model import BaseModel
from app.extensions import db

class Place(BaseModel):
    __tablename__ = "places"  # Must be class-level, not inside __init__
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitute = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, default=False)

    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=None, reviews=None):
        super().__init__()
        self.title = self.validate_name(title, "title", 100)
        self.description = description
        self.price = self.validate_price(price)
        self.latitude = self.validate_coordinate(latitude, "latitude", -90, 90)
        self.longitude = self.validate_coordinate(longitude, "longitude", -180, 180)
        self.owner_id = owner_id
        self.reviews = reviews or []  # List to store related reviews
        self.amenities = amenities or []  # List to store related amenities

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