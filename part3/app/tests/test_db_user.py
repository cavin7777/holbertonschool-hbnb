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
    
    # List all users
    users = facade.get_all_users()
    for user in users:
        print(user.id, user.email)

# (.venv) PS C:\Users\dell\Desktop\Holberton_HBNB\holbertonschool-hbnb\part3> python -m app.tests.c_test_users