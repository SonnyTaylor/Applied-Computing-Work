class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"The {self.make} {self.model} is driving")

    def stop(self):
        print(f"The {self.make} {self.model} has stopped")


car_1 = Car("Kia", "Cerato", 2015, "Blue")

print(car_1)
