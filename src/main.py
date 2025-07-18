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

# Error handling middleware can be added here if needed

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

