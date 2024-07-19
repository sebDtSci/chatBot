import requests
import json


class ApiCall:
    def __init__(self, url, payload, headers):
        self.url = url
        self.payload = payload
        self.headers = headers

    def call_api(self):
        data = json.dumps(self.payload)
        response = requests.post(self.url, headers=self.headers, data=data)
        if response.status_code == 200:
            print("Success!")
            print("Response:", response.json())
        else:
            print("Failed with status code:", response.status_code)
            print("Response:", response.json())
            
    def test_arguments(self):
        if self.payload["contract"]["clients"][0]["nom"] is None:
            print("Il manque le nom du client pour répondre")
        if self.payload["contract"]["clients"][0]["age"] is None:
            print("Il manque l'âge du client pour répondre")
        if self.payload["contract"]["clients"][0]["adresse"] is None:
            print("Il manque l'adresse du client pour répondre")

if __name__ == "__main__":
    
    url = "http://localhost:9090/DecisionService/rest/v1/assurance_deploy/OD_assurance/"
    
    payload = {
        "__DecisionID__": "exampleID",
        "contract": {
            "id": 12345,
            "clients": [
                {
                    "nom": "Dupont",
                    "prenom": "Jean",
                    "age": 23,
                    "adresse": "123 Rue Exemple, Paris"
                }
            ],
            "montant": 0
        }
    }
    headers = {'Content-Type': 'application/json'}

    api = ApiCall(url, payload, headers)
    api.test_arguments()
    api.call_api()
