from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

# Initialize the FastAPI application
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Shopify Insights API"}

# Include API routers
from api.products import router as products_router
from api.policies import router as policies_router
from api.faqs import router as faqs_router
from api.social import router as social_router
from api.contact import router as contact_router

app.include_router(products_router, prefix="/products", tags=["Products"])
app.include_router(policies_router, prefix="/policies", tags=["Policies"])
app.include_router(faqs_router, prefix="/faqs", tags=["FAQs"])
app.include_router(social_router, prefix="/social", tags=["Social"])
app.include_router(contact_router, prefix="/contact", tags=["Contact"])

from fastapi import HTTPException
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup

class BrandInsightsRequest(BaseModel):
    website_url: str

class BrandInsightsResponse(BaseModel):
    product_catalog: list
    hero_products: list
    privacy_policy: str
    return_policy: str
    faqs: list
    social_handles: dict
    contact_details: dict
    about_brand: str
    important_links: dict

@app.post("/brand-insights", response_model=BrandInsightsResponse)
def get_brand_insights(request: BrandInsightsRequest):
    url = request.website_url
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code != 200:
            raise HTTPException(status_code=401, detail="Website not found or inaccessible.")

        soup = BeautifulSoup(resp.text, "html.parser")

        # Product catalog
        try:
            products_resp = requests.get(f"{url.rstrip('/')}/products.json", timeout=10)
            products = products_resp.json().get("products", [])
        except Exception:
            products = []

        # Hero products (from homepage)
        hero_products = [item.text.strip() for item in soup.select('.product, .hero-product')]

        # Privacy Policy
        try:
            pp_resp = requests.get(f"{url.rstrip('/')}/policies/privacy-policy", timeout=10)
            privacy_policy = BeautifulSoup(pp_resp.text, "html.parser").get_text()
        except Exception:
            privacy_policy = "Not found"

        # Return Policy
        try:
            rp_resp = requests.get(f"{url.rstrip('/')}/policies/refund-policy", timeout=10)
            return_policy = BeautifulSoup(rp_resp.text, "html.parser").get_text()
        except Exception:
            return_policy = "Not found"

        # FAQs
        faqs = []
        for faq in soup.select('.faq, .faq-item'):
            question = faq.select_one('.question')
            answer = faq.select_one('.answer')
            if question and answer:
                faqs.append({"question": question.text.strip(), "answer": answer.text.strip()})

        # Social Handles
        social_handles = {}
        for a in soup.find_all('a', href=True):
            href = a['href']
            if "instagram.com" in href:
                social_handles["instagram"] = href
            elif "facebook.com" in href:
                social_handles["facebook"] = href
            elif "tiktok.com" in href:
                social_handles["tiktok"] = href

        # Contact Details
        contact_details = {}
        for a in soup.find_all('a', href=True):
            if "mailto:" in a['href']:
                contact_details["email"] = a['href'].replace("mailto:", "")
            if "tel:" in a['href']:
                contact_details["phone"] = a['href'].replace("tel:", "")

        # About Brand
        about_brand = ""
        about_section = soup.find('section', {'id': 'about'})
        if about_section:
            about_brand = about_section.get_text().strip()
        else:
            about_brand = "Not found"

        # Important Links
        important_links = {}
        for a in soup.find_all('a', href=True):
            if "order-tracking" in a['href']:
                important_links["order_tracking"] = a['href']
            if "contact" in a['href']:
                important_links["contact_us"] = a['href']
            if "blog" in a['href']:
                important_links["blog"] = a['href']

        return BrandInsightsResponse(
            product_catalog=products,
            hero_products=hero_products,
            privacy_policy=privacy_policy,
            return_policy=return_policy,
            faqs=faqs,
            social_handles=social_handles,
            contact_details=contact_details,
            about_brand=about_brand,
            important_links=important_links
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Internal error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
# Error handling middleware can be added here if needed

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

