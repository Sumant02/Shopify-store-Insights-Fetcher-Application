from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    id: int
    title: str
    description: str
    price: float
    image_url: str
    available: bool

class Policy(BaseModel):
    id: int
    title: str
    content: str

class FAQ(BaseModel):
    question: str
    answer: str

class SocialHandle(BaseModel):
    platform: str
    url: str

class ContactDetails(BaseModel):
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None

class ShopifyInsights(BaseModel):
    products: List[Product]
    policies: List[Policy]
    faqs: List[FAQ]
    social_handles: List[SocialHandle]
    contact_details: ContactDetails