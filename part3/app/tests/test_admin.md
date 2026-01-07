# CREATE USERS ADMIN :

Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/users/" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{
    "first_name": "Admin",
    "last_name": "Admin1",
    "email": "admin@example.com",
    "password": "SecurePass123",
    "is_admin": true
  }'