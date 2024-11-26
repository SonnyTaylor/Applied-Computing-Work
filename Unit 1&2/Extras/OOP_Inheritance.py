class Vehicle:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def move(self):
        print("The vehicle is moving.")


class Car(Vehicle):
    def __init__(self, color, speed, number_of_wheels):
        super().__init__(color, speed)
        self.number_of_wheels = number_of_wheels

    def move(self):
        print(
            f"The car with {self.number_of_wheels} wheels is moving at {self.speed} mph."
        )
