import uuid
from datetime import datetime
from app.extensions import db

class BaseModel(db.Model):
    __abstract__ = True  # This ensures SQLAlchemy does not create a table for BaseModel

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    @staticmethod
    def validate_name(value, field_name, max_length):
        if not value or not isinstance(value, str):
            raise ValueError(f"{field_name} must be a non-empty string")
        if len(value) > max_length:
            raise ValueError(f"{field_name} must be at most {max_length} characters")
        return value
    
    @staticmethod
    def validate_coordinate(value, field_name, min_value, max_value):
        if not isinstance(value, (int, float)):
            raise ValueError(f"{field_name} must be a number")
        if not min_value <= value <= max_value:
            raise ValueError(f"{field_name} must be between {min_value} and {max_value}")
        return float(value)
    
    @staticmethod
    def validate_user(value, field_name):
        from .user import User
        if not isinstance(value, User):
            raise ValueError(f"{field_name} must be a User instance")
        return value
    
    @staticmethod
    def validate_place(value, field_name):
        from .place import Place
        if not isinstance(value, Place):
            raise ValueError(f"{field_name} must be a Place instance")
        return value
    
    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Update the updated_at timestamp

    def to_dict(self):
        """Convert model to dictionary"""
        data = {}

        for column in self.__table__.columns:
            value = getattr(self, column.name)

            if isinstance(value, datetime):
                value = value.isoformat()

            data[column.name] = value

        return data