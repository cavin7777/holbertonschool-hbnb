from .base_model import BaseModel
from app.extensions import db, bcrypt
class Amenity(BaseModel):
    __tablename__ = "amenities"  # Must be class-level, not inside __init__
    # Columns
    first_name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        super().__init__()
        self.name = self.validate_name(name, "name", 50)