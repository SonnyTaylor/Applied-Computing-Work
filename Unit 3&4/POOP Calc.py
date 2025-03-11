class Calculator:
    def __init__(self, value=0):
        self.value = value

    def addition(self, number):
        self.value = self.value + number
        return self.value

    def subtraction(self, number):
        self.value = self.value - number
        return self.value

    def multiplication(self, number):
        self.value = self.value * number
        return self.value

    def division(self, number):
        if number != 0:
            self.value = self.value / number
        else:
            raise ValueError("Cannot divide by zero.")
        return self.value

    def reset(self):
        self.value = 0
        return self.value


# Usage examples
calc = Calculator()

# Addition
print(calc.addition(10))  # Output: 10

# Subtraction
print(calc.subtraction(4))  # Output: 6

# Multiplication
print(calc.multiplication(3))  # Output: 18

# Division
print(calc.division(2))  # Output: 9.0

# Reset
print(calc.reset())  # Output: 0
