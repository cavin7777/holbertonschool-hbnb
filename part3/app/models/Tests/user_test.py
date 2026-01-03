from app.models.user import User
from time import sleep

def test_user_creation():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.is_admin is False  # Default value
    print("User creation test passed!")
    print("UUID:", user.id)
    print("Created at:", user.created_at)
    print("Updated at:", user.updated_at)

    sleep(5)
    user.update({"first_name": "Jane"})

    # Print after update
    print("User modification test passed!")
    print("Update name:", user.first_name)
    print("Updated UUID:", user.id)  # UUID does not change
    print("Created at (unchanged):", user.created_at)
    print("Updated at (changed):", user.updated_at)

    user.save()
test_user_creation()
    
sleep(5)

def test_empty_first_name():
    try:
        user = User(first_name="John9999999999999999999999999999999999999999999999999999", last_name="Doe", email="john.doe@example.com")
    except ValueError as e:
        print("Caught expected error:", e)
    else:
        print("Error: No exception raised for empty first_name")

test_empty_first_name()

"""
go to : C:\\Users\dell\Desktop\Holberton_HBNB\holbertonschool-hbnb\hbnb\\
and then : python -m app.models.Tests.user_test
"""