import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"

# -----------------------
# 1️⃣ Create users
# -----------------------
users = [
    {"first_name": "Cavin", "last_name": "Vencadoo", "email": "cavin@test.com", "password": "secret123"},
]

created_users = {}
print("\n--- Creating Users ---")
for u in users:
    res = requests.post(f"{BASE_URL}/users/", json=u)
    if res.status_code == 201:
        data = res.json()
        print(res.status_code, data)
        created_users[u["email"]] = data["id"]
    else:
        print(res.status_code, res.text)

# -----------------------
# 2️⃣ Log in first user
# -----------------------
login_data = {"email": "cavin@test.com", "password": "secret123"}
res = requests.post(f"{BASE_URL}/auth/login", json=login_data)
if res.status_code == 200:
    token = res.json().get("access_token")
    print("\nLogin successful. Token:", token)
else:
    print("\nLogin failed:", res.status_code, res.text)
    exit(1)

headers = {"Authorization": f"Bearer {token}"}

# -----------------------
# 3️⃣ Create amenities
# -----------------------
amenities = [{"name": "Wi-Fi"}, {"name": "TV"}]
created_amenities = {}
print("\n--- Creating Amenities ---")
for a in amenities:
    res = requests.post(f"{BASE_URL}/amenities/", json=a, headers=headers)
    if res.status_code == 201:
        data = res.json()
        print(res.status_code, data)
        created_amenities[a["name"]] = data["id"]
    else:
        print(res.status_code, res.text)

# -----------------------
# 4️⃣ Create places
# -----------------------
places = [
    {
        "title": "Cozy Apartment",
        "description": "Nice and cozy",
        "price": 50.0,
        "latitude": -20.1609,
        "longitude": 57.5012,
        "owner_id": created_users["cavin@test.com"],
        "amenities": list(created_amenities.values())
    },
    {
        "title": "Luxury Villa",
        "description": "Spacious luxury villa",
        "price": 250.0,
        "latitude": -19.8765,
        "longitude": 57.1234,
        "owner_id": created_users["alice@test.com"],
        "amenities": list(created_amenities.values())
    }
]

created_places = {}
print("\n--- Creating Places ---")
for p in places:
    res = requests.post(f"{BASE_URL}/places/", json=p, headers=headers)
    if res.status_code == 201:
        data = res.json()
        print(res.status_code, data)
        created_places[p["title"]] = data["id"]
    else:
        print(res.status_code, res.text)

# -----------------------
# 5️⃣ Update place (only owner can)
# -----------------------
print("\n--- Updating Place ---")
place_id = created_places["Cozy Apartment"]
update_data = {"title": "Cozy Apartment Updated", "description": "Updated description"}
res = requests.put(f"{BASE_URL}/places/{place_id}", json=update_data, headers=headers)
print("Owner update:", res.status_code, res.json())

# Attempt update by non-owner
login_data = {"email": "alice@test.com", "password": "alice123"}
res = requests.post(f"{BASE_URL}/auth/login", json=login_data)
token_alice = res.json().get("access_token")
headers_alice = {"Authorization": f"Bearer {token_alice}"}

update_data = {"title": "Hacked Apartment"}
res = requests.put(f"{BASE_URL}/places/{place_id}", json=update_data, headers=headers_alice)
print("Non-owner update:", res.status_code, res.json())

# -----------------------
# 6️⃣ Create a review (user cannot review own place)
# -----------------------
print("\n--- Creating Reviews ---")
# Make sure Cavin reviews Alice's place (he does NOT own)
review_data = {
    "text": "Great place!",
    "rating": 5,
    "place_id": created_places["Luxury Villa"]  # Owned by Alice
}
res = requests.post(f"{BASE_URL}/reviews/", json=review_data, headers=headers)

if res.status_code == 201:
    review = res.json()
    print("Review created:", res.status_code, review)
    review_id = review["id"]
    
    # -----------------------
    # 7️⃣ Update review
    # -----------------------
    update_review = {"text": "Awesome place!", "rating": 4}
    res = requests.put(f"{BASE_URL}/reviews/{review_id}", json=update_review, headers=headers)
    print("\nUpdate review:", res.status_code, res.json())

    # -----------------------
    # 8️⃣ Delete review
    # -----------------------
    res = requests.delete(f"{BASE_URL}/reviews/{review_id}", headers=headers)
    print("Delete review:", res.status_code, res.json())
else:
    print("Review creation failed:", res.status_code, res.json())


# (.venv) PS C:\Users\dell\Desktop\Holberton_HBNB\holbertonschool-hbnb\part3> python -m app.tests.c_test_users