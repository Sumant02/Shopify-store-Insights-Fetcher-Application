from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_policies():
    # Dummy policies for now
    policies = {
        "privacy_policy": "This is the privacy policy.",
        "return_policy": "This is the return policy."
    }
    return policies