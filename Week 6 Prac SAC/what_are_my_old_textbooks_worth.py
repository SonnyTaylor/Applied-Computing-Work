class Textbook:
    def __init__(self, age, price_paid_for):
        self.age = age
        self.price_paid_for = price_paid_for

    def calculate_current_value(self):
        age_price_mapping = {1: 0.8, 2: 0.6, 3: 0.4, 4: 0.2}

        if self.age >= 5:
            return "The book is worthless"
        elif self.age in age_price_mapping:
            price = self.price_paid_for * age_price_mapping[self.age]
            return f"The current value of the book is ${price:.2f}"
        else:
            return "Invalid age entered"


while True:
    print("Text Book Checker")
    age = input("How old is the book? (years) ")
    price_paid_for = input(
        "How much did you pay for the book? (at the start of the year in $) "
    )

    try:
        age = int(age)
        price_paid_for = float(price_paid_for)
    except ValueError:
        print("Invalid input. Please enter a valid age and price.")
        continue

    textbook = Textbook(age, price_paid_for)
    print("We will pay:")
    print(textbook.calculate_current_value())

    again = input("Would you like to enter another textbook? (y/n) ")
    if again.lower() != "y":
        print("")
        break
    else:
        print("Goodbye!")
        exit()
