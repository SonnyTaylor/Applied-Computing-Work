# Objective: Create a program that asks the user for a number and checks if the number is within a specific range (e.g., 1 to 100). Inform the user if the number is within the range or not.

# This should be a function that accepts a variable and two numbers (min and max value)


def input_in_range(x, min, max):
    if x >= min and x <= max:
        print("The number is within the range")
    else:
        print("The number is not within the range")


user_input = int(input("Enter a number: "))
input_in_range(user_input, 1, 100)
