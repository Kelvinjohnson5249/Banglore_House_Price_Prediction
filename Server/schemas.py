from pydantic import BaseModel

class HouseInput(BaseModel):
    total_sqft: float
    bhk: int
    bath: int
    location: str
