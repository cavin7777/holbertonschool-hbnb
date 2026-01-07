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

## PROTECTED :
Invoke-WebRequest "http://127.0.0.1:5000/api/v1/auth/protected" -Method GET -Headers @{ Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2NzYyMDU5NywianRpIjoiNDBkYmY1NTctNDlhOS00ODUwLTg3OWYtNTUwZTUwY2NmZmI1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImY2NmY2YWI5LTRmMTYtNDczMi04ZTc4LTgwNGI2OGI2YmE5NyIsIm5iZiI6MTc2NzYyMDU5NywiY3NyZiI6Ijk0MzQ2YmYyLThkODAtNDJiNi1iNGVmLWQ2YTM3ZjQ0MWM3MCIsImV4cCI6MTc2NzYyMTQ5NywiaXNfYWRtaW4iOmZhbHNlfQ0Fwna-rzhmvZkGOgrSVE4Oq1uXWeY6i2BTcKGAGHP5c" }

# PUT :

Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/users/c0b53a85-0e51-4a48-a15b-db69dcbd8383" `
  -Method PUT `
  -ContentType "application/json" `
  -Headers @{
    Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2Nzc2NjEyNywianRpIjoiOGI4ZTgzODAtY2Q3OC00YWE4LThmNzAtMWYwZmQ3YzZkNjY0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImMwYjUzYTg1LTBlNTEtNGE0OC1hMTViLWRiNjlkY2JkODM4MyIsIm5iZiI6MTc2Nzc2NjEyNywiY3NyZiI6ImVlMTA3MTgzLTNmYTYtNDkzZi1iZWI0LWNkMTg0OGIyMTI4YyIsImV4cCI6MTc2Nzc2NzAyNywiaXNfYWRtaW4iOmZhbHNlfQ.JHLlp4lo79UgxQsuVQFsggbxoVFbgWwHDkSPGwXjgs4"
  } `
  -Body '{
    "first_name": "cavin1",
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

# PLACE :
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/places/" `
  -Method POST `
  -ContentType "application/json" `
  -Headers @{ Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2NzY4MjM2NywianRpIjoiOGZhYWM2ZDUtMmU5OC00NWU0LWE2NDQtNTQ5OGY0YjU4OTY2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImMwYjUzYTg1LTBlNTEtNGE0OC1hMTViLWRiNjlkY2JkODM4MyIsIm5iZiI6MTc2NzY4MjM2NywiY3NyZiI6IjA1ZDFhYjM1LTI5ZDEtNDBmNC04MWM3LWUyODdkN2UyOTZjNSIsImV4cCI6MTc2NzY4MzI2NywiaXNfYWRtaW4iOmZhbHNlfQ.9cBXqm3k25PnEwBbEfo3iWb6oJmuqJrWKSwFEMNA51c" } `
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
    Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2NzY4MjU4NywianRpIjoiMzUwNjEzODMtMGE1Ni00NGNkLWFhNzEtOWU1ODBmNGZjNjlkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImM0OWM1NWM5LTczMDEtNDFlYS04YzllLTJiOWQ0NjBjMzk0MiIsIm5iZiI6MTc2NzY4MjU4NywiY3NyZiI6IjUzNDgxN2E0LTE3NTItNGQ3OS1hYzE3LTUwZGM0MGQ2MjVlYyIsImV4cCI6MTc2NzY4MzQ4NywiaXNfYWRtaW4iOmZhbHNlfQ.c81vyFzjiJwNgT1EqGYeyOkqjdd0ouyHcUKKyJulEA0"
  } `
  -Body '{
    "text": "Nice",
    "rating": 4,
    "place_id": "3ed4d665-33a9-4693-8012-94d81719e82f"
  }'

