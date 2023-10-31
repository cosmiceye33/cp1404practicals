"""
Guitar Program
Estimated:1h 30m
Actual:1h 3m
"""

from guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar = Guitar(name, year, cost)
other_guitar = Guitar("Another Guitar", 2013, 3009.13)

print(f"{guitar.name} get_age() - Expected 101. Got {guitar.get_age()}")
print(f"{other_guitar.name} get_age() - Expected 10. Got {other_guitar.get_age()}")
print(f"{guitar.name} is_vintage - Expected True. Got {guitar.is_vintage()}")
print(f"{other_guitar.name} is_vintage - Expected False. Got {other_guitar.is_vintage()}")