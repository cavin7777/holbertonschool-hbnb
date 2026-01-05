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
Invoke-WebRequest "http://127.0.0.1:5000/api/v1/auth/protected" -Method GET -Headers @{ Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2NzYyMDU5NywianRpIjoiNDBkYmY1NTctNDlhOS00ODUwLTg3OWYtNTUwZTUwY2NmZmI1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImY2NmY2YWI5LTRmMTYtNDczMi04ZTc4LTgwNGI2OGI2YmE5NyIsIm5iZiI6MTc2NzYyMDU5NywiY3NyZiI6Ijk0MzQ2YmYyLThkODAtNDJiNi1iNGVmLWQ2YTM3ZjQ0MWM3MCIsImV4cCI6MTc2NzYyMTQ5NywiaXNfYWRtaW4iOmZhbHNlfQ0Fwna-rzhmvZkGOgrSVE4Oq1uXWeY6i2BTcKGAGHP5c" }

# PUT :

$token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2NzYyMDg4NiwianRpIjoiOGM3ZjYyZWEtYjU2OS00MjljLWI3YTktZjllMGI3OWU5MDYwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImY2NmY2YWI5LTRmMTYtNDczMi04ZTc4LTgwNGI2OGI2YmE5NyIsIm5iZiI6MTc2NzYyMDg4NiwiY3NyZiI6IjA0NTE1ZmNjLTc3ZDEtNDgyMy1hY2RhLTcwNmVmYzk3YWZmMSIsImV4cCI6MTc2NzYyMTc4NiwiaXNfYWRtaW4iOmZhbHNlfQ.CcIJFLp0Pqy1taZaS6ppvom5kEIsd5-bitnzmKv0F9w"

Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/users/f66f6ab9-4f16-4732-8e78-804b68b6ba97" `
  -Method PUT `
  -ContentType "application/json" `
  -Headers @{ Authorization = "Bearer $token" } `
  -Body '{
    "first_name": "Joe2",
    "last_name": "Barton"
  }'



# PLACE :
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/places/" `
  -Method POST `
  -ContentType "application/json" `
  -Headers @{ Authorization = "Bearer YOUR_JWT_TOKEN_HERE" } `
  -Body '{
        "title": "Cozy Apartment",
        "description": "Nice and cozy",
        "price": 50.0,
        "latitude": -20.1609,
        "longitude": 57.5012,
        "owner_id": created_users["cavin@test.com"],
        "amenities": list(created_amenities.values())
  }'