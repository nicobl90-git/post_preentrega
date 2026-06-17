import requests
import pytest
import time
from utils.loggers import logger

# URL = 'https://jsonplaceholder.typicode.com/posts/1'

payload = {
 'id': 1,
 'title': 'Automation Testing Guide',
 'body': 'Guía completa de testing automatizado',
 'userId': 1
}


@pytest.mark.api
def test_put_post(post_by_id_url):
 URL = post_by_id_url(1)  # Usamos el fixture para obtener la URL del post con ID 1
 payload = {
    'id': 1, 
    'title': 'Automation Testing Guide', 
    'body': 'Guía completa de testing automatizado', 
    'userId': 1
  }
 start = time.time()
 r = requests.put(URL, json=payload)
 assert r.status_code == 200
 body = r.json()
 assert body['title'] == 'Automation Testing Guide'
 assert body['body'] == 'Guía completa de testing automatizado'
 assert body['id'] == 1
 assert r.elapsed.total_seconds() < 1
 print(f"Tiempo de respuesta: {r.elapsed.total_seconds()} segundos")