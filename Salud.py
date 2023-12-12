import requests
import json

def obtener_estado_salud_red(ip, puerto, ticket):
    url = f"http://{ip}:{puerto}/api/v1/assurance/health"
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
ticket = "NC-23-ffaaec7859f24b16a09e-nbi"

estado_salud_red = obtener_estado_salud_red(ip, puerto, ticket)
if estado_salud_red:
    print("Estado de salud de la red obtenido: ", json.dumps(estado_salud_red, ensure_ascii=False))
else:
    print("No se pudo obtener el estado de salud de la red")
