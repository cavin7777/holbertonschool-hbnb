from app.models.place import Place
from app.models.review import Review


def create_places_and_reviews(facade):
    """
    Create default places and reviews on app startup
    """

    # 🔹 Retrieve users
    john = facade.get_user_by_email("john.doe@example.com")
    jane = facade.get_user_by_email("jane.smith@example.com")

    if not john or not jane:
        return  # Users not ready yet

    # 🔹 Retrieve amenities
    wifi = facade.amenity_repo.get_by_attribute("name", "Wi-Fi")
    tv = facade.amenity_repo.get_by_attribute("name", "TV")

    # ==========================
    # 🏠 PLACE 1
    # ==========================
    place1_data = {
        "title": "Beach House",
        "description": "Beautiful house near the sea",
        "price": 150,
        "latitude": -20.348,
        "longitude": 57.552,
        "owner_id": john.id
    }

    place1 = Place(**place1_data)
    if wifi:
        place1.add_amenity(wifi)
    if tv:
        place1.add_amenity(tv)

    facade.place_repo.add(place1)

    # ==========================
    # 🏠 PLACE 2
    # ==========================
    place2_data = {
        "title": "Mountain Cabin",
        "description": "Quiet cabin in the mountains",
        "price": 90,
        "latitude": -20.250,
        "longitude": 57.500,
        "owner_id": jane.id
    }

    place2 = Place(**place2_data)
    if wifi:
        place2.add_amenity(wifi)

    facade.place_repo.add(place2)

    # ==========================
    # ⭐ REVIEWS
    # ==========================
    review1 = Review(
        text="Amazing place, very relaxing!",
        rating=5,
        user=jane,
        place=place1
    )

    review2 = Review(
        text="Clean and comfortable stay.",
        rating=4,
        user=john,
        place=place2
    )

    facade.review_repo.add(review1)
    facade.review_repo.add(review2)
