import requests
import pytest
from utils.loggers import logger

"""
URL = 'https://jsonplaceholder.typicode.com/users'

def test_get_users():
    r = requests.get(URL)
    print(f"\nStatus code: {r.status_code}")
    assert r.status_code == 200

    data = r.json()
    print(f"Cantidad de usuarios: {len(data)}")
    print(f"Primer usuario: {data[0]}")
    assert len(data) > 0
    assert data[0]['id'] == 1
"""

URL = 'https://reqres.in/api/users?page=2'

URL = 'https://reqres.in/api/users?page=2'
API_KEY = 'pro_687a35cc99c02c28f522221f8db090b1f52aceb1bd7134330b4649d5fa579c38'

def test_get_users():
    headers = {'x-api-key': API_KEY}
    r = requests.get(URL, headers=headers)
    # print(f"\nStatus code: {r.status_code}")
    assert r.status_code == 200

    data = r.json()
    # print(f"Página: {data['page']}")
    assert data['page'] == 2
    # print(f"Cantidad de usuarios: {len(data['data'])}")
    assert len(data['data']) > 0
    # print(f"Usuarios: {data['data']}")