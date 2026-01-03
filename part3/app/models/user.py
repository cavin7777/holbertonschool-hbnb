from .base_model import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = self.validate_name(first_name, "first_name",50)
        self.last_name = self.validate_name(last_name, "last_name", 50)
        self.email = self.validate_email(email)
        self.is_admin = bool(is_admin)
   
    @staticmethod
    def validate_email(email):
        if not email or not isinstance(email, str):
            raise ValueError("Email must be a non-empty string")
        if "@" not in email:
            raise ValueError("Invalid email format")
        return email