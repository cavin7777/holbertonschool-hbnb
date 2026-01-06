from .base_model import BaseModel
from app.extensions import db
from app.models.place import place_amenity 
class Amenity(BaseModel):
    __tablename__ = "amenities"  # Must be class-level, not inside __init__
    # Columns
    name = db.Column(db.String(255), nullable=False, unique=True)
    places = db.relationship("Place", secondary=place_amenity, back_populates="amenities")

    def __init__(self, name):
        super().__init__()
        self.name = self.validate_name(name, "name", 50)