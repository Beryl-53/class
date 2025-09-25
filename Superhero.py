class Superhero:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self._health = health  # Protected attribute

    def display_info(self):
        print(f"Name: {self.name}, Power: {self.power}, Health: {self._health}")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

    def get_health(self):
        return self._health

    def set_health(self, value):
        self._health = value

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, health, flight_speed):
        super().__init__(name, power, health)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} flies at {self.flight_speed} km/h!")

    # Polymorphism: override use_power
    def use_power(self):
        print(f"{self.name} soars and uses {self.power} in the sky!")
