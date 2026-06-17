import requests
import pytest
from utils.loggers import logger


# URL = 'https://jsonplaceholder.typicode.com/posts/1'

def test_delete_post(post_by_id_url):
   URL = post_by_id_url(1)  # Usamos el fixture para obtener la URL del post con ID 1
   r = requests.delete(URL)
   assert r.status_code == 200  # JSONPlaceholder devuelve 200, no 204
   # JSONPlaceholder simula la eliminación devolviendo objeto vacío
   body = r.json()
   assert body == {} or 'id' not in body or body['id'] is None
   print("DELETE completado - Recurso eliminado")