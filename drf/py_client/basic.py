import requests

endpoint = 'http://127.0.0.1:8000/api/'

get_response = requests.post(
    endpoint, data={'title': "abc", 'content': 'Hello World', 'price': "123"})  # HTTP Request
print(get_response.json())
# print(get_response.status_code)
