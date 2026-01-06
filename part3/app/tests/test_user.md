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
    "first_name": "",
    "last_name": "Barton"
  }'



# PLACE :
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/places/" `
  -Method POST `
  -ContentType "application/json" `
  -Headers @{ Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2NzY2MjM4MCwianRpIjoiMjIwNDNiMzQtNTMwYy00YmRkLWIyODEtZjdjY2IxOGQ3YjExIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjA3MmIyYWIyLWI2ZjgtNDE1ZS1hMzc1LWM5OWNlNWNhOTU3NyIsIm5iZiI6MTc2NzY2MjM4MCwiY3NyZiI6ImNmOGNiMGM5LWY5ZGUtNGMwMC1iYmU3LWZmODVkYzNkYzMxNiIsImV4cCI6MTc2NzY2MzI4MCwiaXNfYWRtaW4iOmZhbHNlfQ.tRMbCAzlbeMUxq-kpIgVXeSEMCRKKcxN1K5RrAl0Cr0" } `
  -Body '{
        "title": "Cozy Palace",
        "description": "Nice and cozy",
        "price": 500.0,
        "latitude": -30.1609,
        "longitude": -57.5012,
        "amenities": ["TV"]
  }'

Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/reviews/" `
  -Method POST `
  -ContentType "application/json" `
  -Headers @{ 
    Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2NzY2MzU4OCwianRpIjoiZWIyZTNlYTMtMzY1Yy00ODE4LTljYTQtNWJkNzgyNWEwNjlhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjA3MmIyYWIyLWI2ZjgtNDE1ZS1hMzc1LWM5OWNlNWNhOTU3NyIsIm5iZiI6MTc2NzY2MzU4OCwiY3NyZiI6IjI1NmMxOWUxLTcxYzgtNGU4ZC04MDBkLTc2N2NhYTIwMDg2NCIsImV4cCI6MTc2NzY2NDQ4OCwiaXNfYWRtaW4iOmZhbHNlfQ.vdg1Pi4hbDywKd5OZPZk1HxvUqmFBRyxXIk5VxrlISw"
  } `
  -Body '{
    "text": "Nice",
    "rating": 4,
    "place_id": "4ff6507b-0e30-46c2-a4a4-d4e039918434"
  }'

{
  "first_name": "Joe",
  "last_name": "Dan",
  "email": "dan@gmail.com",
  "password": "dan123"
}