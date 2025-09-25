class Animal:
    def move(self):
        print("walking")

class Car:
    def move(self):
        print("flying")

class Boat:
    def move(self):
        print("sailing")

# Usage
objects = [Animal(), Car(), Boat()]
for obj in objects:
    obj.move()
