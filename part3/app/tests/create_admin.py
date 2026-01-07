# create_admin.py
from app import create_app
from app.services import facade


admin_data = {
    "first_name": "Admin",
    "last_name": "Admin1",
    "email": "admin@example.com",
    "password": "SecurePass123",
    "is_admin": True
}

app = create_app()

# Run inside application context
with app.app_context():
    # Check if admin already exists
    existing_user = facade.get_user_by_email(admin_data["email"])
    if existing_user:
        print("Admin user already exists")
    else:
        admin_user = facade.create_user(admin_data)
        print(f"Admin created with ID: {admin_user.id}")

# python -m app.tests.create_admin
# Admin created with ID: d8d2ef1b-d512-4f96-a549-24104e8f443f
