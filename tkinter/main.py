import tkinter
import random

# GUI with a label, button, and entry field


def main():
    root = tkinter.Tk()
    root.title("Hello World!")
    root.geometry("400x300")  # Set the window size to 400x300

    label = tkinter.Label(
        root, text="Hello World!", fg="white", bg="black", font=("Arial", 24)
    )
    label.pack()

    another_label = tkinter.Label(
        root, text="Hello Again!", fg="red", bg="yellow", font=("Arial", 18)
    )
    another_label.pack()

    entry = tkinter.Entry(root, fg="blue", bg="white", font=("Arial", 12))
    entry.pack()

    def submit():
        input_text = entry.get()
        label.config(text="You entered: " + input_text)
        label.config(fg=random.choice(["red", "green", "blue", "yellow", "purple"]))
        label.config(bg=random.choice(["black", "white", "gray", "pink", "orange"]))
        label.config(font=("Arial", random.randint(12, 36), "bold"))

    submit_button = tkinter.Button(
        root, text="Submit", command=submit, fg="white", bg="green", font=("Arial", 14)
    )
    submit_button.pack()

    quit_button = tkinter.Button(
        root, text="Quit", command=root.quit, fg="white", bg="red", font=("Arial", 14)
    )
    quit_button.pack()

    def flash_label():
        label.config(fg=random.choice(["red", "green", "blue", "yellow", "purple"]))
        label.config(
            bg=random.choice(
                ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
            )
        )
        label.config(font=("Arial", random.randint(12, 36), "bold"))
        root.after(500, flash_label)

    flash_label()

    root.mainloop()


# Call the main function to display the window
main()
