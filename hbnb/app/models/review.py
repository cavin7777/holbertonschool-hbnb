import uuid
from datetime import datetime

class Review:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.text = str()
        self.rating = int()
        self.place = str() # to change
        self.user = str() # to change
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Update the updated_at timestamp