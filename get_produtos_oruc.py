import os
import json
import requests

url = "https://www.meudatacenter.com/api/v1/produtos"

store_id = os.getenv('store_id')
token = os.getenv('token')

headers = {
    "x-ID": store_id,
    "x-Token": token,
    "Content-Type": "application/json"
    }

response = requests.get(url, headers=headers)
if response.status_code == 200 or response.status_code == 201:
    with open("json-response.txt", "a") as jsonFile:
        jsonFile.write(json.dumps(response.json(), indent=2))
    print("Resposta do servidor:\n", json.dumps(response.json(), indent=2))
else:
    print("Erro: ", response.text)
