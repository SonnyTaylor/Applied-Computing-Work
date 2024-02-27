def factorial(n):
    # Intentional bug: initialization should be 1 for factorial calculation
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    number = 5
    print(f"The factorial of {number} is {factorial(number)}")
