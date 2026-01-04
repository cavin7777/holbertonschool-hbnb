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

Invoke-WebRequest "http://127.0.0.1:5000/api/v1/auth/protected" -Method GET -Headers @{ Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2NzQ3NDg5MiwianRpIjoiMTIyZTNkOWUtYzI3NS00MDEyLTgxMDMtNGI4NzMyNjc4M2VjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImZlODE5ZGMzLWZmYmItNDZhYi05NzIzLTQyMDFiNjI0NDQ2YiIsIm5iZiI6MTc2NzQ3NDg5MiwiY3NyZiI6IjI2ZmU1NDBiLWM4MzItNDZiNy04ZDBmLTA1NTU3OTdkZmMxYiIsImV4cCI6MTc2NzQ3NTc5MiwiaXNfYWRtaW4iOmZhbHNlfQ.HlHNDf6yzqDftclvPbYfuil-J0FDqSm8DTfXpBlInc0" }

