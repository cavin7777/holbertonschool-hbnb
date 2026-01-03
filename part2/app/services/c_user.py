from app.models.user import User
from app.models.amenity import Amenity

def create_users(facade):
    """Create default users on app startup"""
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com"
        },
        {
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane.smith@example.com"
        }
    ]

    for data in users:
        # Avoid duplicate emails if app reloads
        if not facade.get_user_by_email(data["email"]):
            user = User(**data)
            facade.user_repo.add(user)

def create_amenities(facade):
    """Create default amenities on app startup"""
    amenities = [
        {"name": "Wi-Fi",},
        {"name": "TV",}
    ]

    for data in amenities:
        # Avoid duplicate amenities on reload
        existing = facade.amenity_repo.get_by_attribute("name", data["name"])
        if not existing:
            amenity = Amenity(**data)
            facade.amenity_repo.add(amenity)