import requests

SHEETY_API = "YOUR_API"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_API)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode" : city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_API}/{city['id']}",
                json=new_data
            )
            print(response.text)
