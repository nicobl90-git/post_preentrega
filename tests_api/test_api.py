import requests
from utils.loggers import logger

resp = requests.get('https://api.github.com/')
print(resp.status_code) # 200 = OK
print(resp.headers['content-type']) # application/json
payload = resp.json()
print(payload['current_user_url'])
# Importante: resp.json() hace el deserializado automático: 
# #transforma la cadena JSON en estructura Python para que asserts y comparaciones sean sencillos.


# Para correr el ejemplo solo debes ejecutar: python3 nombre_del_archivo.py