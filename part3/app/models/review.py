from .base_model import BaseModel
from .user import User
from .place import Place
from app.extensions import db

class Review(BaseModel):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey("places.id"), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", backref="reviews")
    place = db.relationship("Place", back_populates="reviews")
    
    def __init__(self, text, rating, place: Place, user: User):
        super().__init__()
        self.text = self.validate_name(text, "text", 500)
        self.rating = rating
        self.place = place
        self.user = user

        if not isinstance(rating, int) or not 1 <= rating <= 5:
            raise ValueError("Rating must be an integer between 1 and 5")
