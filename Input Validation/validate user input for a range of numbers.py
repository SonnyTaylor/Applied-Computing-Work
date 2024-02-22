# 1. Ask students to write a Python program that prompts the user for a number between 1 and 100.
# 2. Validate the input by checking if it's a numeric value and within the specified range.
# 3. Display a message indicating whether the input is valid or not.

user_num = int(input("Enter a number between 1 and 100: "))
if 1 <= user_num <= 100:
    print("Number is valid")
else:
    print("Number is not valid")
