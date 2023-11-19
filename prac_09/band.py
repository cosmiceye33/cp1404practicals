"""Band class"""


class Band:
    def __init__(self, name=''):
        self.name = name
        self.musicians = []

    def __repr__(self):
        for musician in self.musicians:
            return f"{self.name} {musician}"

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            if not musician.instruments:
                return f"{musician.name} needs and instrument"
            else:
                return f"{musician.name} is playing {musician.instruments}"

