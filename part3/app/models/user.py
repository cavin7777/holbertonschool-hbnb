import uuid
from datetime import datetime
from app import bcrypt

class User:
    def __init__(self, first_name, last_name, email, is_admin=False):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.password = None
    
        if not first_name or len(first_name) > 50:
            raise ValueError("first_name is required and must be <= 50 characters")

        if not last_name or len(last_name) > 50:
            raise ValueError("last_name is required and must be <= 50 characters")

        if not email or "@" not in email:
            raise ValueError("A valid email address is required")

        # Relationship with place
        self.places = []
    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Update the updated_at timestamp

    def hash_password(self, password):
        """Hashes the password before storing it."""
        truncated = password[:72] 
        self.password = bcrypt.generate_password_hash(truncated).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        truncated = password[:72]
        return bcrypt.check_password_hash(self.password, truncated)
