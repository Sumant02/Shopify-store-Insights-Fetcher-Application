from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_social():
    social_handles = {
        "instagram": "https://instagram.com/yourbrand",
        "facebook": "https://facebook.com/yourbrand"
    }
    return {"social_handles": social_handles}