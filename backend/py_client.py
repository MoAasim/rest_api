
# request package is not installed

import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/auth" #127.0.0.1
password = getpass()

auth_response = requests.post(auth_endpoint, json={'username':'moham', 'password': password})
print(auth_response.json())


if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f"Token {token}"
    }
    endpoint = "http://localhost:8000/api/products/" #127.0.0.1

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())