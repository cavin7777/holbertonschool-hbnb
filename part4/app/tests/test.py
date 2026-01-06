from app import create_app, db
from app.models.user import User

app = create_app()
with app.app_context():
    user = User.query.filter_by(email="john.doe@example.com").first()
    if user:
        print("User exists:", user.email)
        print("Stored password hash:", user.password)
    else:
        print("User not found")

from werkzeug.security import check_password_hash

# Replace <stored_hash> with the printed hash
check_password_hash("<stored_hash>", "password123") 

from werkzeug.security import check_password_hash

stored_hash = "scrypt:32768:8:1$vGSCPKi43fHKgDVI$aa6dbf93e3b3014fe5d400dfe0452424a34d1afee3d85c86bdc9ed0f48ecf1f0922f0d471916ea5d6e66c3f43e43e9f4cd878e9f44dfebc37263fd9316a5ac4c"
password_to_test = "password123"

print(check_password_hash(stored_hash, password_to_test))