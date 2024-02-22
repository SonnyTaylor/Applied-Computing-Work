# 1. Write a Python program that prompts the user for a password.
# 2. Create a custom validation function that checks if the password meets the following criteria:
#    ○ At least 8 characters long
#    ○ Contains at least one uppercase letter
#    ○ Contains at least one lowercase letter
#    ○ Contains at least one digit
# 3. Display a message indicating whether the input is valid or not.


def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True


user_passwd = input("Enter your password: ")
if validate_password(user_passwd):
    print("Valid password")
else:
    print("Invalid password")
    print(
        "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit."
    )
