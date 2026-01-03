from .base_model import BaseModel
class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = self.validate_name(name, "name", 50)