from fastapi import APIRouter
from services.data_organizer import DataOrganizer

router = APIRouter()

@router.get("/")
def get_products():
    organizer = DataOrganizer()
    # Dummy products list for now
    products = [
        {"id": 1, "name": "Product 1"},
        {"id": 2, "name": "Product 2"}
    ]
    return {"products": organizer.organize(products)}