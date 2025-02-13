# Importing required libraries
import math


# Functions for calculating area and perimeter
def rectangle_area(length, width):
    return length * width


def rectangle_perimeter(length, width):
    return 2 * (length + width)


def triangle_area(base, height):
    return (base * height) / 2


def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3


# Main program
print("Welcome to the Geometry Calculator!")
shape = input("Enter the shape ('rectangle' or 'triangle'): ")

if shape.lower() == "rectangle":
    length = input("Enter the length: ")
    width = input("Enter the width: ")

    area = rectangle_area(length, width)
    perimeter = rectangle_perimeter(length, width)

    print("Area: ", area, " Perimeter: ", perimeter)

elif shape.lower() == "triangle":
    side1 = input("Enter the first side: ")
    side2 = input("Enter the second side: ")
    side3 = input("Enter the third side: ")

    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    perimeter = triangle_perimeter(side1, side2, side3)

    print("Area: ", area, " Perimeter: ", perimeter)

else:
    print("Invalid shape. Please enter either 'rectangle' or 'triangle'.")
