import requests
import pytest
from utils.loggers import logger

# URL = 'https://jsonplaceholder.typicode.com/posts/1'

PATCH_PAYLOAD = { 'title': 'Título actualizado por PATCH' }

@pytest.mark.api
def test_patch_post(post_by_id_url):
   URL = post_by_id_url(1)  # Usamos el fixture para obtener la URL del post con ID 1
   r = requests.patch(URL, json=PATCH_PAYLOAD)
   assert r.status_code == 200
   body = r.json()
   assert body['title'] == 'Título actualizado por PATCH'
   # El resto de campos se mantienen
   assert 'body' in body
   assert 'userId' in body
   print(f"PATCH completado - Solo título actualizado")