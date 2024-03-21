t = int(input("What is the temperature: "))
if t > 35:
    x = "very hot"
elif t > 25:
    x = "warm"
elif t > 20:
    x = "perfect"
elif t < 20:
    x = "cold"
else:
    print("invalid input")
