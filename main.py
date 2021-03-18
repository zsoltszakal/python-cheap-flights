from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

sheet_data = data_manager.get_destination_data()
# print(sheet_data)

if sheet_data[0]["iataCode"] == "":

    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()


tomorrow = datetime.now() + timedelta(days=1)
six_month = datetime.now() + timedelta(days=180)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month

    )

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            text=f"Low Price Alert! Only {flight.price} to fly from {flight.origin_city}-{flight.origin_airport}."
