from pydantic import BaseModel

class Marker(BaseModel):
    latlng: tuple[float, float]
    shape: str
    name: str
    location_type: str = ""
    color: str = "#000000"
