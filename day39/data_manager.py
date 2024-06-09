import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()
sheety_endpoint = os.getenv("SHEETY_ENDPOINT")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = os.environ["SHEETY_USER"]
        self._pwd = os.environ["SHEETY_PWD"]
        self.authorization = HTTPBasicAuth(self._user, self._pwd)
        self.flight_data = {}

    def get_flight_data(self):
        res = requests.get(url=sheety_endpoint)
        data = res.json()
        self.flight_data = data["prices"]

        return self.flight_data

    def update_flight_data(self):
        for row in self.flight_data:
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            res = requests.put(
                url=f"{sheety_endpoint}/{row['id']}",
                json=new_data
            )
            print(res.text)
