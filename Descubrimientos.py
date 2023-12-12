import requests
import json

def obtener_descubrimientos(ip, puerto, ticket_api):
    url = f"http://{ip}:{puerto}/api/v1/discovery"
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
print(obtener_descubrimientos('127.0.0.1', '58000', 'NC-9-cce79debb5914227b6cf-nbi'))
