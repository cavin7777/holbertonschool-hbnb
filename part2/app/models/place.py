from app.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=None):
        super().__init__()
        self.title = self.validate_name(title, "title", 100)
        self.description = description
        self.price = self.validate_price(price)
        self.latitude = self.validate_coordinate(latitude, "latitude", -90, 90)
        self.longitude = self.validate_coordinate(longitude, "longitude", -180, 180)
        self.owner_id = owner_id
        self.reviews = []  # List to store related reviews
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