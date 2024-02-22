def is_valid_name(name):
    return name.isalpha() and len(name) > 0

def is_valid_age(age):
    return age.isdigit() and 1 <= int(age) <= 120

def is_valid_email(email):
    return '@' in email and '.' in email

def collect_user_inputs():
    inputs = {}
    while True:
        first_name = input("Enter your first name: ")
        if is_valid_name(first_name):
            inputs['First Name'] = first_name
            break
        else:
            print("Invalid first name. Please try again.")

    while True:
        last_name = input("Enter your last name: ")
        if is_valid_name(last_name):
            inputs['Last Name'] = last_name
            break
        else:
            print("Invalid last name. Please try again.")

    while True:
        age = input("Enter your age: ")
        if is_valid_age(age):
            inputs['Age'] = int(age)
            break
        else:
            print("Invalid age. Please try again.")

    while True:
        email = input("Enter your email address: ")
        if is_valid_email(email):
            inputs['Email'] = email
            break
        else:
            print("Invalid email address. Please try again.")

    return inputs

user_inputs = collect_user_inputs()
print(user_inputs)
