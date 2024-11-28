age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You are not born yet!")
else:
    print("You must be 18+ to sign up")
