import requests
import json

def obtener_credenciales(ip, puerto, ticket_api):
    url = f"http://{ip}:{puerto}/api/v1/global-credential/cli"
    headers = {"X-Auth-Token": ticket_api}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if isinstance(data, dict) and 'response' in data:
            return json.dumps(data['response'], indent=4)
        else:
            return "La respuesta no está en el formato esperado."
    else:
        return f"Error: {response.status_code}"

# Reemplaza 'IP', 'PUERTO' y 'TICKET_API' con tus valores
print(obtener_credenciales('127.0.0.1', '58000', 'NC-23-ffaaec7859f24b16a09e-nbi'))
