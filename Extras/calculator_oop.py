class Calculator:
    """
    A simple calculator class with methods for addition, subtraction, multiplication, and division.
    """

    def add(self, num1, num2):
        """
        Adds two numbers and returns the result.
        """
        return num1 + num2

    def subtract(self, num1, num2):
        """
        Subtracts the second number from the first number and returns the result.
        """
        return num1 - num2

    def multiply(self, num1, num2):
        """
        Multiplies two numbers and returns the result.
        """
        return num1 * num2

    def divide(self, num1, num2):
        """
        Divides the first number by the second number and returns the result.
        """
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")


# Example usage:
# Create an instance of the Calculator class
calc = Calculator()

while True:
    print("\nSimple Calculator")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == "+":
            result = print(calc.add(num1, num2))
        elif operation == "-":
            result = print(calc.subtract(num1, num2))
        elif operation == "*":
            result = print(calc.multiply(num1, num2))
        elif operation == "/":
            result = print(calc.divide(num1, num2))
        else:
            result = "Invalid operation"

    # invalid input error handling
    except ValueError as e:
        print("Invalid input:", e)
