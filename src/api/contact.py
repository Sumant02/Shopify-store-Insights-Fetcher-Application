from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_contact():
    contact_details = {
        "email": "contact@yourbrand.com",
        "phone": "+1234567890"
    }
    return {"contact_details": contact_details}