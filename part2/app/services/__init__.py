from app.services.facade import HBnBFacade
from app.services.c_user import create_users, create_amenities
from app.services.c_others import create_places_and_reviews

facade = HBnBFacade()
create_users(facade)
create_amenities(facade)
create_places_and_reviews(facade)