"""
Debes validar los siguientes datos: → email eve.holt@reqres.in, password cityslicka, esperar 200 y token

Datos inválidos → email sin password, esperar 400 

Usar @pytest.mark.parametrize con los casos
"""

import requests
import pytest
from utils.loggers import logger

LOGIN_URL = 'https://reqres.in/api/login'
API_KEY = 'pro_687a35cc99c02c28f522221f8db090b1f52aceb1bd7134330b4649d5fa579c38'

@pytest.mark.api 
@pytest.mark.parametrize("email, password, expected_status", [
    ('eve.holt@reqres.in', 'cityslicka', 200)
])
def test_login(email, password, expected_status):
    headers = {'x-api-key': API_KEY}
    creds = {'email': email, 'password': password}
    resp = requests.post(LOGIN_URL, json=creds, headers=headers)
    assert resp.status_code == expected_status

    body = resp.json()
    assert 'token' in body

@pytest.mark.api
@pytest.mark.parametrize("email, password, expected_status", [
    ('eve.holt@reqres.in', '', 400)
])
def test_login_invalid_credentials(email, password, expected_status):
    headers = {'x-api-key': API_KEY}
    creds = {'email': email, 'password': password}
    resp = requests.post(LOGIN_URL, json=creds, headers=headers)
    assert resp.status_code == expected_status

    body = resp.json()
    assert 'token' not in body