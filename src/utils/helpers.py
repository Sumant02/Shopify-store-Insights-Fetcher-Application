def fetch_json(url):
    import requests
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def parse_product_data(data):
    if not data or 'products' not in data:
        return []
    return [
        {
            'id': product.get('id'),
            'title': product.get('title'),
            'price': product.get('variants', [{}])[0].get('price'),
            'description': product.get('body_html'),
            'image': product.get('images', [{}])[0].get('src'),
        }
        for product in data['products']
    ]

def parse_policy_data(data):
    if not data:
        return {}
    return {
        'privacy_policy': data.get('privacy_policy'),
        'return_policy': data.get('refund_policy'),
    }

def parse_faq_data(data):
    if not data or 'faqs' not in data:
        return []
    return [{'question': faq.get('question'), 'answer': faq.get('answer')} for faq in data['faqs']]

def parse_social_data(data):
    if not data:
        return {}
    return {
        'facebook': data.get('facebook'),
        'twitter': data.get('twitter'),
        'instagram': data.get('instagram'),
    }

def parse_contact_data(data):
    if not data:
        return {}
    return {
        'email': data.get('email'),
        'phone': data.get('phone'),
    }