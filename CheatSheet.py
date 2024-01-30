# Python Cheat Sheet

# Variable:
variable = 1 # Integer variable
variable = 1.0 # Float variable
variable = "1" # String variable
variable = True # Boolean variable


# Control Flow:
if variable == 1:
    print("Variable is equal to 1")
elif variable == 2:
    print("Variable is equal to 2")
else:
    print("Variable is not equal to 1 or 2")
    
    
# Loop:
for i in range(10):
    print(i)
    
    
# Function:
def function_name(parameter_1, parameter_2):
    return parameter_1 + parameter_2


# List:
list = [1, 2, 3, 4, 5]


# Dictionary:
dictionary = {
    "key_1": "value_1",
    "key_2": "value_2",
    "key_3": "value_3"
}


# Tuple:
tuple = (1, 2, 3, 4, 5)
# Set:
set = {1, 2, 3, 4, 5}


# Class:
class ClassName:
    def __init__(self, parameter_1, parameter_2):
        self.parameter_1 = parameter_1
        self.parameter_2 = parameter_2
    def function_name(self):
        return self.parameter_1 + self.parameter_2
    
    
# Import:
import module_name
from module_name import function_name


# File I/O:
file = open("file_name.txt", "r")
file = open("file_name.txt", "w")
file = open("file_name.txt", "a")
file = open("file_name.txt", "r+")
file.close()


# Exception Handling:
try:
    print(variable)
except:
    print("An exception occurred")
finally:
    print("The 'try except' is finished")
    
    
# Regular Expression:
import re
re.search("pattern", "string")
re.findall("pattern", "string")
re.sub("pattern", "replace", "string")


# Math:
import math
math.pi
math.e
math.sin(1)
math.cos(1)


# Random:
import random
random.random()
random.randint(1, 10)
random.choice([1, 2, 3, 4, 5])


# Datetime:
import datetime
datetime.datetime.now()
datetime.datetime(2024, 1, 1)