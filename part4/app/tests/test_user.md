## USERS
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/users/" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{
    'first_name': 'Super',
    'last_name': 'Admin',
    'email': 'admin@example.com',
    'password': 'SecurePass123',
  }'

# LOGIN :
  {
  "email": "vencadoo@gmail.com",
  "password": "string123"
}

## PROTECTED :
Invoke-WebRequest "http://127.0.0.1:5000/api/v1/auth/protected" -Method GET -Headers @{ Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2NzYyMDU5NywianRpIjoiNDBkYmY1NTctNDlhOS00ODUwLTg3OWYtNTUwZTUwY2NmZmI1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImY2NmY2YWI5LTRmMTYtNDczMi04ZTc4LTgwNGI2OGI2YmE5NyIsIm5iZiI6MTc2NzYyMDU5NywiY3NyZiI6Ijk0MzQ2YmYyLThkODAtNDJiNi1iNGVmLWQ2YTM3ZjQ0MWM3MCIsImV4cCI6MTc2NzYyMTQ5NywiaXNfYWRtaW4iOmZhbHNlfQ0Fwna-rzhmvZkGOgrSVE4Oq1uXWeY6i2BTcKGAGHP5c" }

# PUT :

Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/users/36b1890a-7e6d-4846-9fbe-f1f0689ae887" `
  -Method PUT `
  -ContentType "application/json" `
  -Headers @{
    Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2Nzk0MjQxMCwianRpIjoiNDczNDk5MDktMjFhMC00OGJhLWJhYTktZmViOTYxZjIzYjI0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjM2YjE4OTBhLTdlNmQtNDg0Ni05ZmJlLWYxZjA2ODlhZTg4NyIsIm5iZiI6MTc2Nzk0MjQxMCwiY3NyZiI6ImYxZmY1ZjQ5LTQ4YmYtNGZhMy05MGQwLWIzNWY3NDEyYzMxMyIsImV4cCI6MTc2Nzk0MzMxMCwiaXNfYWRtaW4iOmZhbHNlfQ.4v3Z1ccwpvp_r-QkNBRRe7EenZqOsn8bnEghrcdI8nA"
  } `
  -Body '{
    "first_name": "cavin3",
    "last_name": "vencadoo"
  }'
# NO DATA FOUND
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/users/USER_A_ID" `
  -Method PUT `
  -ContentType "application/json" `
  -Headers @{
    Authorization = "Bearer USER_B_JWT_TOKEN"
  } `
  -Body "{}"

# Unauthorized action
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/users/c49c55c9-7301-41ea-8c9e-2b9d460c3942" `
  -Method PUT `
  -ContentType "application/json" `
  -Headers @{
    Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2Nzc2NDgxOSwianRpIjoiYzkyZjdlYTItNDgwOC00ZTEwLTlkMTItNTJiNjVmNjg0ODc5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImMwYjUzYTg1LTBlNTEtNGE0OC1hMTViLWRiNjlkY2JkODM4MyIsIm5iZiI6MTc2Nzc2NDgxOSwiY3NyZiI6IjhkMjMwOTg5LTE0ZDQtNDIxNi05YjI4LWZhZWViNGI1ZmM5MCIsImV4cCI6MTc2Nzc2NTcxOSwiaXNfYWRtaW4iOmZhbHNlfQ.p6sWwHD8KIqLdUuS_IQwXlm2dB9YezsLvNeHMqnsTTw"
  } `
  -Body "{}"

# POST PLACE :
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/places/" `
  -Method POST `
  -ContentType "application/json" `
  -Headers @{ Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2Nzk0NDExOSwianRpIjoiYzU4NWFhNWItNDU2ZS00MTY4LTgxMDgtNmNiYjRiMGMwMzY4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjM2YjE4OTBhLTdlNmQtNDg0Ni05ZmJlLWYxZjA2ODlhZTg4NyIsIm5iZiI6MTc2Nzk0NDExOSwiY3NyZiI6ImVjNDBiNDM5LTdmOWMtNGRmNy05OWY3LWIzYjgzMWRhMTMyNCIsImV4cCI6MTc2Nzk0NTAxOSwiaXNfYWRtaW4iOmZhbHNlfQ.dUPdcSpj7XgpmIN-MH13FlQ6K-HgbrPj5pAXnEgiVk8" } `
  -Body '{
        "title": "Cozy Palace",
        "description": "Nice and cozy",
        "price": 500.0,
        "latitude": -30.1609,
        "longitude": -57.5012,
        "amenities": ["TV"]
  }'

# PUT PLACE : 
Invoke-RestMethod `
   -Uri "http://127.0.0.1:5000/api/v1/places/8c60502a-96b6-4dad-8dfc-f7b5414a76b9" `
   -Method PUT `
   -ContentType "application/json" `
   -Headers @{ Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2Nzk0NjE2OCwianRpIjoiOTdhNjBmODctZTM4My00MTJlLWExNWItNDQxN2MyNjZjMTAzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjM2YjE4OTBhLTdlNmQtNDg0Ni05ZmJlLWYxZjA2ODlhZTg4NyIsIm5iZiI6MTc2Nzk0NjE2OCwiY3NyZiI6IjUwYjM4ODAxLWQ1MzgtNDU2ZS05YmZiLTdlZGRjMDU1YjYxYSIsImV4cCI6MTc2Nzk0NzA2OCwiaXNfYWRtaW4iOmZhbHNlfQ.d9Ic3-20c4WjZB87ilnWlk_MuoRm2AN87qIV1C5xlj4" } `
   -Body '{
         "title": "Cozy Palace_1",
         "description": "Nice and cozy",
         "price": 500.0,
   }'

# POST REVIEW
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/reviews/" `
  -Method POST `
  -ContentType "application/json" `
  -Headers @{ 
    Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2Nzk1MDk1NiwianRpIjoiNTE1MmJlMjItMzEwNy00NTY5LTlmZWEtMzJlYTE1MDlkMzI3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjhkMTc2OTA4LTFhODItNDNhYi04YmY0LTM4YTBiMzAyNTY0NCIsIm5iZiI6MTc2Nzk1MDk1NiwiY3NyZiI6IjA2Y2ZiMTdjLWM5NzItNDI0Yi05ODkxLTYxMzg4YWQ5NGE1NyIsImV4cCI6MTc2Nzk1MTg1NiwiaXNfYWRtaW4iOmZhbHNlfQ.C9kU4llJ45w9KWotid8mfASQc7zMJOv5QNAHGwl36Qw"
  } `
  -Body '{
    "text": "Nice",
    "rating": 4,
    "place_id": "8c60502a-96b6-4dad-8dfc-f7b5414a76b9"
  }'

