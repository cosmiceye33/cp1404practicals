from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self. fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odo={self._odometer} {self.get_fare()} on current fare, ${self.price_per_km}/km plus fagfall of ${self.flagfall}"

    def get_fare(self):
        return self.flagfall +super().get_fare()
