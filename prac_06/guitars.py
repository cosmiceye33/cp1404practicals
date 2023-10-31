"""
Guitar Program
Estimated:1h 30m
Actual:1h 3m
"""

from guitar import Guitar

GREETING = "My Guitars!"

guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print(f"{new_guitar} added.")
    name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

if guitars:
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage = "" if guitar.is_vintage() else "(vintage)"
        print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:10,.2f} {vintage}")
else:
    print("Get a guitar!")