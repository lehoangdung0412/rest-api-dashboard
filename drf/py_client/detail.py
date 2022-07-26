import requests

endpoint = 'http://127.0.0.1:8000/api/products/2/'

get_response = requests.get(endpoint)  # HTTP Request
print(get_response.json())
# print(get_response.status_code)
