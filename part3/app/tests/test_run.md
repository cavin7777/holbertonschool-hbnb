C:\Users\dell\Desktop\Holberton_HBNB\holbertonschool-hbnb\hbnb> 

python -m app.tests.test_user

Invoke-RestMethod -Uri http://localhost:5000/api/v1/users/ `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"}'


id                                   first_name last_name email
--                                   ---------- --------- -----
fc409abb-fa7f-41c3-814b-a0d2fc2d8f4f John       Doe       john.doe@example.com

Invoke-RestMethod -Uri http://localhost:5000/api/v1/amenities/ `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"name": "Wi-Fi"}'


id                                   name 
--                                   ----
23adfff6-422a-4a14-95d4-d1b83496c806 Wi-Fi     

Invoke-RestMethod -Uri http://localhost:5000/api/v1/places/ `
  -Method POST `
  -ContentType "application/json" `
  -Body '{
    "title": "Cozy Apartment",
    "description": "A nice place to stay",
    "price": 100.0,
    "latitude": 37.7749,
    "longitude": -122.4194,
    "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "amenities": []
  }'
