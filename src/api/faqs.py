from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_faqs():
    faqs = [
        {"question": "Do you have COD as a payment option?", "answer": "Yes, we do have"},
        {"question": "How can I track my order?", "answer": "Use the order tracking link on our website."}
    ]
    return {"faqs": faqs}