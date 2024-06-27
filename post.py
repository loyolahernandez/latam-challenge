import requests
import json


url = "https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/data-engineer"


data = {
    "name": "Ignacio Loyola",
    "mail": "ignacioloyolah@gmail.com",
    "github_url": "https://github.com/loyolahernandez/latam-challenge"
}


json_data = json.dumps(data)


headers = {
    "Content-Type": "application/json"
}


response = requests.post(url, data=json_data, headers=headers)


if response.status_code == 200:
    print("POST request enviado correctamente.")
else:
    print(f"Error al enviar POST request: {response.status_code} - {response.text}")
