"""
Envía POST /api/users con distintos nombres y trabajos 

Usa parametrización (puede ser con datos fijos o Faker) 

Comprueba 201 y que createdAt incluya el año actual
"""

import requests
import pytest
from faker import Faker
from utils.loggers import logger

fake = Faker('es_ES')

URL = 'https://reqres.in/api/users'
API_KEY = 'pro_687a35cc99c02c28f522221f8db090b1f52aceb1bd7134330b4649d5fa579c38'

@pytest.mark.api 
@pytest.mark.parametrize("name, job", [
    (fake.name(), fake.job())
])

def test_create_user(name, job):
    headers = {'x-api-key': API_KEY}
    payload = {'name': name, 'job': job}
    r = requests.post(URL, json=payload, headers=headers)
    assert r.status_code == 201

    new_user = r.json()
    assert new_user['name'] == name
    assert 'id' in new_user and 'createdAt' in new_user

