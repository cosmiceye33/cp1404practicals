
"""
Guitar Program
Estimated:1h 30m
Actual:1h 3m
"""
CURRENT_YEAR = 2023
VINTAGE_AGE = 50
class Guitar:
    """Guitar class"""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a string of guitar"""
        return f"{self.name} {self.year} : {self.cost}"


    def get_age(self):

        """Get the age of a guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine is a guitar is vintage"""
        return self.get_age() >= VINTAGE_AGE