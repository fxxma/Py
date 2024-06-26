# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_flight_data()

flight_search = FlightSearch()
if sheet_data[0]["iataCode"] == "":

    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["iataCode"])
    # print(f"sheet_data:\n{sheet_data}")

data_manager.update_flight_data()
