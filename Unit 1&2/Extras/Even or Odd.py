def check_odd_or_even(number):
    match number % 2:
        case 0:
            return "Even"
        case _:
            return "Odd"
