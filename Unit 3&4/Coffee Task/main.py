import os
from colorama import init, Fore, Style

# colorama isnt needed but it probs wont run without it
# its also really pretty

init(autoreset=True)

coffee_prices = {
    "Espresso": 2.50,
    "Americano": 3,
    "Latte": 2.50,
    "Cappuccino": 3,
    "Macchiato": 2.50,
    "Mocha": 3.50,
    "Flat White": 2.50,
}

size_prices = {
    "Medium": 0,
    "Large": 1.00,
    "XL": 1.50,
}


def clear_terminal():
    """Clears the terminal screen."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_border(text, width=35):
    """Prints a border around the text.

    Args:
        text (string): The text to be displayed.
        width (int, optional): _description_. Defaults to 35.
    """
    print(Fore.CYAN + "+" + "-" * (width - 2) + "+")
    print(Fore.CYAN + "|" + text.center(width - 2) + "|")
    print(Fore.CYAN + "+" + "-" * (width - 2) + "+")


def print_menu():
    """Prints the coffee shop menu."""
    clear_terminal()
    print("\n")
    print_border("The Coffee Shop")
    print(Fore.YELLOW + Style.BRIGHT + "\n             Welcome!\n")
    print("We serve the following coffees:")
    coffees = [
        "1. Espresso",
        "2. Americano",
        "3. Latte",
        "4. Cappuccino",
        "5. Macchiato",
        "6. Mocha",
        "7. Flat White",
    ]
    for coffee in coffees:
        print(Fore.GREEN + " > " + coffee)
    print("-" * 40)


def get_coffee_choice():
    """Prompts the user to select a coffee.

    Returns:
        int: The user's coffee selection
    """
    while True:
        try:
            choice = int(input(Fore.YELLOW + "\nWhat coffee would you like? (1-7): "))
            if 1 <= choice <= 7:
                return choice
        except ValueError:
            pass
        print(Fore.RED + "Invalid selection. Please try again.")


def select_coffee(coffee_selection_num):
    """Returns the name of the coffee based on the selection number.

    Args:
        coffee_selection_num (int): The user's coffee selection number.

    Returns:
        string: The name of the coffee selected.
    """
    match coffee_selection_num:
        case 1:
            return "Espresso"
        case 2:
            return "Americano"
        case 3:
            return "Latte"
        case 4:
            return "Cappuccino"
        case 5:
            return "Macchiato"
        case 6:
            return "Mocha"
        case 7:
            return "Flat White"


def select_coffee_size(coffee_selection):
    """Prompts the user to select a coffee size.

    Args:
        coffee_selection (string): The name of the coffee selected.

    Returns:
        string: The size of the coffee
    """
    while True:
        print("\n" + Fore.CYAN + "Choose your Coffee Size:")
        print(Fore.GREEN + " M - Medium (No Extra)")
        print(Fore.GREEN + " L - Large (+$1.00)")
        print(Fore.GREEN + " XL - XL (+$1.50)")
        size_input = input(
            Fore.YELLOW + f"What size for {coffee_selection}? (M, L, XL): "
        ).upper()
        if size_input in ["M", "L", "XL"]:
            return {"M": "Medium", "L": "Large", "XL": "XL"}[size_input]
        else:
            print(Fore.RED + "Invalid selection. Please try again.")


def eat_in_or_takeaway():
    """Prompts the user to select whether the coffee is for takeaway or eat in.

    Returns:
        string: The type of order (Takeaway or Eat in)
    """
    while True:
        response = input(
            Fore.YELLOW + "Would you like your coffee for takeaway? (Yes/No): "
        ).lower()
        if response in ["yes", "no"]:
            return "Takeaway" if response == "yes" else "Eat in"
        else:
            print(Fore.RED + "Invalid selection. Please enter Yes or No.")


def main():
    """Main function to run the coffee shop program."""
    print_menu()
    try:
        num_cups = int(input(Fore.YELLOW + "How many coffees are being ordered? "))
    except ValueError:
        print(Fore.RED + "Invalid number. Exiting.")
        return

    total_order_price = 0
    order_details = []  # Store details for each order

    for i in range(num_cups):
        # Get coffee choice, size, and order type
        print(Fore.BLUE + f"\nEntering details for coffee #{i+1}:")
        coffee_choice_num = get_coffee_choice()
        coffee_choice = select_coffee(coffee_choice_num)
        coffee_size = select_coffee_size(coffee_choice)
        order_type = eat_in_or_takeaway()

        base_price = coffee_prices[coffee_choice]
        size_extra = size_prices[coffee_size]
        coffee_price = base_price + size_extra
        takeaway_extra = 0
        if order_type == "Takeaway":
            takeaway_extra = 1
            coffee_price += takeaway_extra

        total_order_price += coffee_price

        # Store order info for detailed summary
        order_details.append(
            {
                "coffee": coffee_choice,
                "size": coffee_size,
                "order_type": order_type,
                "base_price": base_price,
                "size_extra": size_extra,
                "takeaway_extra": takeaway_extra,
                "total": coffee_price,
            }
        )

    clear_terminal()
    print("\n")
    print_border("Order Summary")

    # Detailed summary for each coffee order
    for idx, order in enumerate(order_details, start=1):
        print(Fore.MAGENTA + f"\nCoffee #{idx}: {order['coffee']}")
        print(
            Fore.GREEN + f"   Size: {order['size']} (Extra: ${order['size_extra']:.2f})"
        )
        print(
            Fore.GREEN
            + f"   Order Type: {order['order_type']} (Takeaway Extra: ${order['takeaway_extra']:.2f})"
        )
        print(Fore.GREEN + f"   Base Price: ${order['base_price']:.2f}")
        print(Fore.CYAN + f"   Total: ${order['total']:.2f}")

    print(
        Fore.BLUE + f"\nTotal price for {num_cups} coffee(s): ${total_order_price:.2f}"
    )
    print(Fore.YELLOW + "\nThank you for your order. Enjoy your coffee!\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\nExiting program.")
        exit(0)
