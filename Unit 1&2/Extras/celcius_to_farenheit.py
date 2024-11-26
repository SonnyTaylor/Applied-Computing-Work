def celcius_to_farenheit(celcius):
    """Converts celcius to farenheit

    Args:
        celcius (float): The temperature in celcius

    Returns:
        float: Tempature in farenheit
    """
    farenheit = (celcius * 9 / 5) + 32
    return farenheit


def main():
    celcius = float(input("Enter temperature in celcius: "))
    farenheit = celcius_to_farenheit(celcius)
    print(f"{celcius}°C is equal to {farenheit}°F.")


main()
