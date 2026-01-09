# CREATE USERS WITH ADMIN :

# POST USER :
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/admin/users/" `
  -Method POST `
  -ContentType "application/json" `
  -Headers @{
    Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2Nzk0MTc5NCwianRpIjoiZTc5OGRkMzctOGU0Yi00ZjNkLWIzNzEtYTc4NWViMjQ3MzFmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjJmYTUyNWZhLTZiMjMtNDY0NS04NjhlLTIxMzcwZjE2NTIxNCIsIm5iZiI6MTc2Nzk0MTc5NCwiY3NyZiI6ImNlMjE5YjE3LWU4MjAtNDgxMC1iMzNmLTZiMmZkMTM1MmJjYyIsImV4cCI6MTc2Nzk0MjY5NCwiaXNfYWRtaW4iOnRydWV9.of6DahK-nkFJOupukqxjmodo8_lnzdZKgr5ccDAzMVU"
  } `
  -Body '{
    "first_name": "Micheal",
    "last_name": "Jordan",
    "email": "jordan@gmail.com",
    "password": "jordan123"
  }'


# PUT USER:
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/admin/users/2e61ac2e-18e3-47b8-9d29-3ae73afb892e" `
  -Method PUT `
  -ContentType "application/json" `
  -Headers @{
    Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2Nzk0MTc5NCwianRpIjoiZTc5OGRkMzctOGU0Yi00ZjNkLWIzNzEtYTc4NWViMjQ3MzFmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjJmYTUyNWZhLTZiMjMtNDY0NS04NjhlLTIxMzcwZjE2NTIxNCIsIm5iZiI6MTc2Nzk0MTc5NCwiY3NyZiI6ImNlMjE5YjE3LWU4MjAtNDgxMC1iMzNmLTZiMmZkMTM1MmJjYyIsImV4cCI6MTc2Nzk0MjY5NCwiaXNfYWRtaW4iOnRydWV9.of6DahK-nkFJOupukqxjmodo8_lnzdZKgr5ccDAzMVU"
  } `
  -Body '{
    "first_name": "Micheal_1",
    "last_name": "Jordan",
    "email": "jordan@gmail.com",
    "password": "jordan123"
  }'

# POST AMENITY :
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/admin/amenities/" `
  -Method POST `
  -ContentType "application/json" `
  -Headers @{
      Authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2Nzk0MzMwNywianRpIjoiYzAwMGZiZGEtMGFmNi00MWFkLTk2NWItODIzNDc3OTVmZWVkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjJmYTUyNWZhLTZiMjMtNDY0NS04NjhlLTIxMzcwZjE2NTIxNCIsIm5iZiI6MTc2Nzk0MzMwNywiY3NyZiI6IjcyOGQxNWY2LTFlN2QtNDg4Ny05ZDRlLTJlNTNhYTg5MGM3MSIsImV4cCI6MTc2Nzk0NDIwNywiaXNfYWRtaW4iOnRydWV9._xF4-M3XG7RGH4x_DaK8Rh0DExdMgZdJZof2jZ5QGnA"
  } `
  -Body '{
    "name": "Jacuzi"
  }'

  # PUT AMENITY : 
  Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/v1/admin/amenities/YOUR_AMENITY_ID" `
  -Method PUT `
  -ContentType "application/json" `
  -Headers @{
      Authorization = "Bearer YOUR_ADMIN_JWT_TOKEN"
  } `
  -Body '{
    "name": "High-Speed WiFi"
  }'