from fastapi import APIRouter
from Server.schemas import HouseInput
from Server.load_model import get_estimated_price, get_locations as load_locations


router = APIRouter()

@router.get("/locations")
def get_locations():
    return {"locations": load_locations()}

@router.post("/predict")
def predict_price(data: HouseInput):
    result = get_estimated_price(
        data.location,
        data.total_sqft,
        data.bhk,
        data.bath
    )
    return {"estimated_price": result}
