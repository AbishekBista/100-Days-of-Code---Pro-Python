from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "DAL"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_months  =datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    flight = flight.search.check_flights(ORIGIN_CITY_IATA, destination['iataCode'], from_time=tomorrow, to_time=six_months)

    if flight == None:
        continue

    if flight.price < destination["lowestPrice"]:
        message=f"Low price alert! Only {flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport},from {flight.out_date} to {flight.return_date}."
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)
        
        notification_manager.send_emails(emails, message)
