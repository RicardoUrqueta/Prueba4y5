import requests

def obtener_ticket():
    url = "http://localhost:58000/api/v1/ticket"
    headers = {
        "content-type": "application/json"
    }
    data = {
        "username": "admin",
        "password": "admin123!"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["response"]["serviceTicket"]
    else:
        return None

ticket = obtener_ticket()
if ticket:
    print("Ticket obtenido: ", ticket)
else:
    print("No se pudo obtener el ticket")
