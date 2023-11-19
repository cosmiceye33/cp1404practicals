from silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Fancy taxi", 100, 2)
taxi.drive(18)
print(taxi)
print(taxi.get_fare())