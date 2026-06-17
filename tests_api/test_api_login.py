import requests
from utils.loggers import logger


LOGIN_URL = 'https://reqres.in/api/login'
API_KEY = 'pro_687a35cc99c02c28f522221f8db090b1f52aceb1bd7134330b4649d5fa579c38'

def test_login_successful():
    headers = {'x-api-key': API_KEY}
    creds = {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
    resp = requests.post(LOGIN_URL, json=creds, headers=headers)
    #print(f"\nStatus code: {resp.status_code}")
    assert resp.status_code == 200

    body = resp.json()
    # print(f"Respuesta completa: {body}")
    assert 'token' in body
    # print(f"Token recibido: {body['token']}")