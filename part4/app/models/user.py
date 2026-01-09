from .base_model import BaseModel
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
# from sqlalchemy.dialects.mysql import LONGTEXT

class User(BaseModel):
    __tablename__ = "users"  # Must be class-level, not inside __init__
    # Columns
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = self.validate_name(first_name, "first_name",50)
        self.last_name = self.validate_name(last_name, "last_name", 50)
        self.email = self.validate_email(email)
        self.is_admin = bool(is_admin)
        self.hash_password(password)

    @property
    def first_name_value(self):
        return self.first_name
    @first_name_value.setter
    def first_name_value(self, value):
        self.first_name = self.validate_name(value, "first_name", 50)

    @property
    def last_name_value(self):
        return self.last_name
    @last_name_value.setter
    def last_name_value(self, value):
        self.last_name = self.validate_name(value, "last_name", 50)

    @staticmethod
    def validate_email(email):
        if not email or not isinstance(email, str):
            raise ValueError("Email must be a non-empty string")
        if "@" not in email:
            raise ValueError("Invalid email format")
        return email

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = generate_password_hash(password)
    
    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return check_password_hash(self.password, password)