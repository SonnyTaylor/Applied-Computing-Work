with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


def write_to_file_with_user_input():
    """asks user for input and writes it to a file"""

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    fav_color = input("Enter your favorite color: ")
    with open("user_info.txt", "w") as file:
        file.write(f"Name: {name}\nAge: {age}\nFavorite Color: {fav_color}")
    print("File written successfully.")


if __name__ == "__main__":

    write_to_file_with_user_input()
