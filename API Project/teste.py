# Esse arquivo ira testar a requisição ao servidor localhost
# é necessario rodar o arquivo Flask_Rest_API.py e depois esse arquivo teste.py
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld/bill")
print(response.json())

# continuar video aos  22 minutos