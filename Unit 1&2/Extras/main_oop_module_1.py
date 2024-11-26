from oop_module_1 import *

my_car = Car("Toyota", "Corolla", 2015, "Red")

print("My car: ")
print(my_car.make)
print(my_car.model)
print(my_car.year)
print(my_car.color)
my_car.drive()
my_car.stop()

my_other_car = Car("Ford", "Fiesta", 2018, "Blue")
print("\nMy other car: ")
print(my_other_car.make)
print(my_other_car.model)
print(my_other_car.year)
print(my_other_car.color)
my_other_car.drive()    
my_other_car.stop()