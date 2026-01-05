Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/users/" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{
    "first_name": "Cavin",
    "last_name": "Vencadoo",
    "email": "cavin@test.com",
    "password": "secret123"
  }'

# LOGIN :
  {
  "email": "vencadoo@gmail.com",
  "password": "string123"
}

# PROTECTED :
Invoke-WebRequest "http://127.0.0.1:5000/api/v1/auth/protected" -Method GET -Headers @{ Authorization = "Bearer TOKEN" }

Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/users/158d0615-c335-4b01-b6b5-7b26d030e235" `
  -Method PUT `
  -ContentType "application/json" `
  -Headers @{ Authorization = "Bearer TOKEN" } `
  -Body '{
    "first_name": "Cavin2",
    "last_name": "Vencadoo"
  }'

# PLACE :
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/places/" `
  -Method POST `
  -ContentType "application/json" `
  -Headers @{ Authorization = "Bearer YOUR_JWT_TOKEN_HERE" } `
  -Body '{
    "name": "My First Place",
    "description": "Nice apartment near the beach",
    "city_id": "city-uuid-here",
    "owner_id": "158d0615-c335-4b01-b6b5-7b26d030e235",
    "price": 120
  }'