# 1. Write a Python program that prompts the user for an email address.
# 2. Validate the email address by checking if it contains the '@' and '.' characters.
# 3. Display a message indicating whether the input is valid or not.

users_email = input("Enter your email: ")
if "@" in users_email and "." in users_email:
    print("Email is valid")
else:
    print("Email is not valid")
