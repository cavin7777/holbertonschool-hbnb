from werkzeug.security import generate_password_hash
from app import create_app, db
from app.models.user import User

app = create_app()

with app.app_context():
    user = User.query.filter_by(email="roger@example.com").first()
    if user:
        user.password = generate_password_hash("roger123")  # set the password you want
        db.session.commit()
        print("✅ Password reset successfully")
    else:
        print("User not found")
