from unreliable_car import UnreliableCar

my_car = UnreliableCar("Barina", 100, 30)
other_car = UnreliableCar("Mega Mobile", 100, 90)
for i in range(1, 5):
    print(f"{my_car.name} drove {my_car.drive(i)}km")
    print(f"{other_car.name} drove {other_car.drive(i)}km")

