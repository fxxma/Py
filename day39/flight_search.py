import os
import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["AMADEUS_KEY"]
        self._api_secret = os.environ["AMADEUS_SECRET"]
        self._token = self._get_new_token()

    def get_destination_code(self, city_name):
        code = "TESTING"
        return code

    def _get_new_token(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant-type": "client_credentials",
            "client_id": os.environ["AMADEUS_KEY"],
            "client_secret": os.environ["AMADEUS_SECRET"]
        }
        res = requests.post(url=os.environ["AMADEUS_TOKEN_ENDPOINT"], headers=header, data=body)

        print(res.text)
        return res












