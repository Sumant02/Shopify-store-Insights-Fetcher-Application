class ShopifyClient:
    def __init__(self, shop_url, access_token):
        self.shop_url = shop_url
        self.access_token = access_token
        self.base_url = f"https://{shop_url}/admin/api/2023-01"

    def _get_headers(self):
        return {
            "X-Shopify-Access-Token": self.access_token,
            "Content-Type": "application/json"
        }

    def fetch_products(self):
        url = f"{self.base_url}/products.json"
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json().get('products', [])

    def fetch_policies(self):
        url = f"{self.base_url}/policies.json"
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json().get('policies', [])

    def fetch_faqs(self):
        # Assuming FAQs are stored as a custom page or metafield
        url = f"{self.base_url}/pages.json?title=FAQs"
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json().get('pages', [])

    def fetch_social_handles(self):
        # Assuming social handles are stored in a custom app or metafield
        url = f"{self.base_url}/metafields.json"
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json().get('metafields', [])

    def fetch_contact_details(self):
        # Assuming contact details are stored in the shop's settings
        url = f"{self.base_url}/shop.json"
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json().get('shop', {}).get('contact_email', ''), response.json().get('shop', {}).get('phone', '')