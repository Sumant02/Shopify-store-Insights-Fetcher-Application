class DataOrganizer:
    def __init__(self):
        pass

    def organize_product_catalog(self, products):
        organized_products = []
        for product in products:
            organized_products.append({
                "id": product.get("id"),
                "title": product.get("title"),
                "price": product.get("variants")[0].get("price"),
                "description": product.get("body_html"),
                "images": [image.get("src") for image in product.get("images", [])]
            })
        return organized_products

    def organize_policies(self, policies):
        organized_policies = {
            "privacy_policy": policies.get("privacy_policy"),
            "return_policy": policies.get("return_policy"),
            "shipping_policy": policies.get("shipping_policy")
        }
        return organized_policies

    def organize_faqs(self, faqs):
        organized_faqs = []
        for faq in faqs:
            organized_faqs.append({
                "question": faq.get("question"),
                "answer": faq.get("answer")
            })
        return organized_faqs

    def organize_social_handles(self, social_handles):
        organized_handles = {
            "facebook": social_handles.get("facebook"),
            "twitter": social_handles.get("twitter"),
            "instagram": social_handles.get("instagram"),
            "linkedin": social_handles.get("linkedin")
        }
        return organized_handles

    def organize_contact_details(self, contact_details):
        organized_contact = {
            "email": contact_details.get("email"),
            "phone": contact_details.get("phone")
        }
        return organized_contact