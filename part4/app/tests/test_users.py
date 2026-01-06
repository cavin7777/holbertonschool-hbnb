import requests
import jwt


BASE_URL = "http://127.0.0.1:5000/api/v1"

# --------------------------------------
# 1️⃣ Log in first user to get JWT Token
# -------------------------------------
login_data = {"email": "jonathan.doe@example.com", "password": "newpassword456"}
res = requests.post(f"{BASE_URL}/auth/login", json=login_data)
if res.status_code == 200:
    token = res.json().get("access_token")
    print("\nLogin successful. Token:", token)
else:
    print("\nLogin failed:", res.status_code, res.text)
    exit(1)

headers = {"Authorization": f"Bearer {token}"}

res = requests.post(f"{BASE_URL}/auth/login", json=login_data)
if res.status_code != 200:
    raise Exception(f"Login failed: {res.status_code} {res.text}")

login_data = res.json()
token_payload = jwt.decode(token, options={"verify_signature": False})

# Get user ID from login response
# Make sure your login endpoint returns {"access_token": "...", "user_id": "..."}
user_id = token_payload["sub"]  # This is the identity you used when creating the token
if not user_id:
    raise Exception("Login response must include user_id for update test")

headers = {"Authorization": f"Bearer {token}"}
print("✅ Logged in, JWT token obtained")
print("User ID from login:", user_id)

# -----------------------------
# 2️⃣ Update user info
# -----------------------------
update_payload = {
    "first_name": "Jonathan",
    "last_name": "Doe-Smith",
    "email": "jonathan.doe@example.com",
    "password": "newpassword456"
}

res = requests.put(f"{BASE_URL}/users/{user_id}", json=update_payload, headers=headers)
if res.status_code == 200:
    updated_user = res.json()
    print("✅ User updated successfully")
    print(updated_user)
else:
    print("❌ User update failed:", res.status_code, res.text)

# -----------------------------
# 3️⃣ Verify update by logging in again
# -----------------------------
login_payload_new = {
    "email": "jonathan.doe@example.com",
    "password": "newpassword456"
}

res = requests.post(f"{BASE_URL}/auth/login", json=login_payload_new)
if res.status_code == 200:
    print("✅ Re-login successful with updated credentials")
    print("New JWT token:", res.json()["access_token"])
else:
    print("❌ Re-login failed:", res.status_code, res.text)
