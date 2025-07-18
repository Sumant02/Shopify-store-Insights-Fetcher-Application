# Shopify Insights App

## Overview
The Shopify Insights App is a Python application built using FastAPI that fetches and organizes insights from a given Shopify store's website. It provides a structured way to access product catalogs, policies, FAQs, social media handles, and contact details.

## Features
- Fetch product catalog and hero products
- Retrieve privacy and return/refund policies
- Access frequently asked questions (FAQs)
- Get social media handles of the brand
- Fetch contact details such as email and phone numbers

## Project Structure
```
shopify-insights-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── api                    # API endpoints for various data
│   │   ├── products.py        # Product-related endpoints
│   │   ├── policies.py        # Policy-related endpoints
│   │   ├── faqs.py            # FAQ-related endpoints
│   │   ├── social.py          # Social media endpoints
│   │   └── contact.py         # Contact information endpoints
│   ├── services               # Services for data fetching and organization
│   │   ├── shopify_client.py  # Shopify client for API requests
│   │   └── data_organizer.py  # Data organization logic
│   ├── models                 # Data models for validation
│   │   └── schemas.py         # Pydantic schemas
│   └── utils                  # Utility functions
│       └── helpers.py         # Helper functions for data handling
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Files to ignore in version control
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd shopify-insights-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
uvicorn src.main:app --reload
```

## API Endpoints
- **Products**: `/api/products`
- **Policies**: `/api/policies`
- **FAQs**: `/api/faqs`
- **Social Media**: `/api/social`
- **Contact**: `/api/contact`

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.