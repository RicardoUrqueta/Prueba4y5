import requests
import json

def obtener_problemas_red(ip, puerto, ticket):
    url = f"http://{ip}:{puerto}/api/v1/assurance/health-issues"
    headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Reemplaza estas variables con tus valores reales
ip = "127.0.0.1"
puerto = "58000"
ticket = "NC-9-cce79debb5914227b6cf-nbi"

problemas_red = obtener_problemas_red(ip, puerto, ticket)
if problemas_red:
    print("Problemas de la red obtenidos: ", json.dumps(problemas_red, ensure_ascii=False))
else:
    print("No se pudo obtener los problemas de la red")
