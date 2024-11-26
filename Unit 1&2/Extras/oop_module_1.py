class Car:
    # Class variables
    wheels = 4
    
    # Class attributes and constructer
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        
    # Class method
    def drive(self):
        print(f"The {self.year} {self.make} {self.model} is driving.")
        
    def stop(self):
        print(f"The {self.year} {self.make} {self.model} is stopping.")