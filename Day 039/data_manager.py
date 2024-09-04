from pprint import pprint
import requests
from secret import SHEETY_ENDPOINT, SHEET_ENDPOINT_CUSTOMER



class DataManager:

    def __init__(self):
        self.destination_data = {}
    
    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)
    
    def get_customer_email(self):
        customer_endpoint = SHEET_ENDPOINT_CUSTOMER
        response = requests.get(customer_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data