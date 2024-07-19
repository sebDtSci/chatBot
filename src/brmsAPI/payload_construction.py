
def payload_construction(nom,prenom,age,adresse):
    payload = {
            "__DecisionID__": "exampleID",
            "contract": {
                "id": 12345,
                "clients": [
                    {
                        "nom": nom,
                        "prenom": prenom,
                        "age": age,
                        "adresse": adresse
                    }
                ],
                "montant": 0
            }
        }

    return payload