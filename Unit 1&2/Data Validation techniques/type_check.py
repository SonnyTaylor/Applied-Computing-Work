# Objective: Write a function that accepts an input and prints a message depending on the type of the input (integer, string, or list).
# Instructions:
# 	1. Define a function named check_type that takes one argument.
# 	2. Inside the function, use isinstance() to check the type of the argument.
# 	3. Print a message identifying the type: "This is an integer", "This is a string", or "This is a list".
# Test the function with different types of inputs.


def check_type(x):
    if isinstance(x, int):
        print("This is an integer")
    elif isinstance(x, str):
        print("This is a string")
    elif isinstance(x, list):
        print("This is a list")
    elif isinstace(x, float):
        print("This is a float")
    elif isinstance(x, bool):
        print("This is a boolean")
    elif isinstance(x, tuple):
        print("This is a tuple")
    elif isinstance(x, set):
        print("This is a set")
    elif isinstance(x, dict):
        print("This is a dictionary")
    else:
        print("This is a different type")


check_type(5)
check_type("hello")
check_type([1, 2, 3])
check_type(5.5)
check_type(True)
check_type((1, 2, 3))
check_type({1, 2, 3})
check_type({"name": "John", "age": 30})
