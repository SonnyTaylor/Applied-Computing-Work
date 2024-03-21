# t = int(input("What is the temperature: "))
# if t > 35:
#     x = "Very hot"
# elif t > 25:
#     x = "Warm"
# elif t > 20:
#     x = "Perfect"
# elif t < 20:
#     x = "Cold"
# else:
#     print("Invalid input")


t = int(input("What is the temperature: "))
if t > 35:
    x = "Very hot"
else:
    if t > 25:
        x = "Warm"
    else:
        if t > 20:
            x = "Perfect"
        else:
            if t < 20:
                x = "Cold"
            else:
                print("Invalid input")
