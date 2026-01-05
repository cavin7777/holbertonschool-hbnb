from app import create_app, db
from app.models.user import User

app = create_app()

with app.app_context():
    db.create_all()  # Create tables in HBNB
"""
# Create a user
    user = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        password="password123",
        is_admin=False
    )

    db.session.add(user)
    db.session.commit()

        # Print user info
    print(f"User created with ID: {user.id}")
    print(f"Email: {user.email}")
    print(f"Hashed password: {user.password}")
"""

from app.services.facade import HBnBFacade

app = create_app()

with app.app_context():
    facade = HBnBFacade()
    
    place_data = {
        "title": "Beach House",
        "description": "Nice house near the beach",
        "price": 150.0,
        "latitude": -20.3484,
        "longitude": 57.5522,
        "owner_id": "f1bdcf02-17fa-417b-bea3-315d8a839620"
    }

    place = facade.create_place(place_data)
    print(place.id)

# (.venv) PS C:\Users\dell\Desktop\Holberton_HBNB\holbertonschool-hbnb\part3> python -m app.tests.test_db_user