print("Temperature Converter")
while True:
    print("1. Celcius to Farenheight")
    print("2. Farenheight to Celcius")
    choice = input("Enter choice: ")

    # Celcius to Farenheight
    if choice == "1":
        celcius = float(input("Enter temperature in Celcius: "))
        farenheight = (celcius * 9 / 5) + 32
        print(f"Temperature in Farenheight: {farenheight}")
        continue_choice = input("Do you want to continue? (y/n): ")
        if continue_choice == "n":
            break
        elif continue_choice == "y":
            continue

    # Farenheight to Celcius
    elif choice == "2":
        farenheight = float(input("Enter temperature in Farenheight: "))
        celcius = (farenheight - 32) * 5 / 9
        print(f"Temperature in Celcius: {celcius}")
        continue_choice = input("Do you want to continue? (y/n): ")
        if continue_choice == "n":
            break
        elif continue_choice == "y":
            continue
    else:
        print("Invalid choice")
