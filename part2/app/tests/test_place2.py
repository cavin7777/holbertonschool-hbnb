from app.models.place import Place
from app.models.user import User


u = User("John", "Doe", "john@example.com")
p = Place("Nice House", "A cozy place", 100, 10.0, 20.0, u)
print(p.to_dict_basic())
