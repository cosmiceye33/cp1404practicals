from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "Q)uit, C)hoose taxt, D)rive"

def main():
    total_bill = 0
    taxis = [Taxi("Barina Mobile", 100), SilverServiceTaxi("BEAST", 100, 2), SilverServiceTaxi("The Taxi", 100, 4)]
    current_taxi = None
    print("Let's Drive")
    print(MENU)
    choice = input(">>> "). lower()

