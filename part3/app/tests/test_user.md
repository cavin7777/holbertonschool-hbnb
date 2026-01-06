## USERS
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

Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/users/c0b53a85-0e51-4a48-a15b-db69dcbd8383" `
  -Method PUT `
  -ContentType "application/json" `
  -Headers @{
    Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2NzY4MDI3NywianRpIjoiMjc4M2Y5MzMtOTAyMy00MzNmLTkyODktZjRhY2M4OGQ1OTQ2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImMwYjUzYTg1LTBlNTEtNGE0OC1hMTViLWRiNjlkY2JkODM4MyIsIm5iZiI6MTc2NzY4MDI3NywiY3NyZiI6IjFiNjRmYTljLTgzMjQtNGExYy1hNWI3LWMyZTQ5Y2I2MTg0NSIsImV4cCI6MTc2NzY4MTE3NywiaXNfYWRtaW4iOmZhbHNlfQ.XJ79tsU1lzWuIJDDg7b3CXwK__pXMRz2JA247rEamvU"
  } `
  -Body '{
    "first_name": "cavin",
    "last_name": ""
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

# REVIEW
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/reviews/" `
  -Method POST `
  -ContentType "application/json" `
  -Headers @{ 
    Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2NzY2Mzc0NSwianRpIjoiMWM4NzUwZjMtODJmYS00MTM0LTk3MjQtZDAzNjMxMjlhMWNkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Ijk0MzVmN2U4LThmMjktNDY2Ny1iOWYwLWVkNTQ5NzI5OTY3YSIsIm5iZiI6MTc2NzY2Mzc0NSwiY3NyZiI6ImE3OGY3ZWRiLWIwNGUtNGJmMC04ODgxLWEwZDE2YjYwZmM2NyIsImV4cCI6MTc2NzY2NDY0NSwiaXNfYWRtaW4iOmZhbHNlfQ.TxB8aO9sMeMic33S1L76MgQIKod5haSJnIkzVv4gDZE"
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