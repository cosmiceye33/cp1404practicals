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
    while choice != "q":
        if choice == "c":
            print("Available Taxis")
            display_taxis(taxis)
            taxi_choice = int(input("Choose Taxi"))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi:
                current_taxi.get_fare()
                distance_driven = float(input("Drive how far?"))
                current_taxi.drive(distance_driven)
                cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
                total_bill += cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost : ${total_bill:.2f}")
    print(f"Taxis are now:")
    print(display_taxis(taxis))

def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()


