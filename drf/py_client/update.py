import requests

endpoint = 'http://127.0.0.1:8000/api/products/3/update/'

data = {
    "title": "This field is updated by mixin views",
    "price": 129.99
}

get_response = requests.put(endpoint, data=data)  # HTTP Request
print(get_response.json())
# print(get_response.status_code)
