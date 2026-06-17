"""
Hace GET a /api/users?page=1 y verifica que cada usuario tenga las claves id, email, first_name, last_name 

Extra: validar que el avatar termina en .jpg
"""

import requests
import pytest
from utils.loggers import logger

URL = 'https://reqres.in/api/users?page=2'
API_KEY = 'pro_687a35cc99c02c28f522221f8db090b1f52aceb1bd7134330b4649d5fa579c38'

@pytest.mark.api
def test_get_users():
    headers = {'x-api-key': API_KEY}
    r = requests.get(URL, headers=headers)
    assert r.status_code == 200

    data = r.json()
    for user in data['data']:
        assert 'id' in user
        assert 'email' in user
        assert 'first_name' in user
        assert 'last_name' in user
        # Extra: validar que el avatar termina en .jpg
        assert user['avatar'].endswith('.jpg')

    print(f"Página: {data['page']}")
    
    assert data['page'] == 2
    print(f"Cantidad de usuarios: {len(data['data'])}")
    
    assert len(data['data']) > 0
    print(f"Usuarios: {data['data']}")