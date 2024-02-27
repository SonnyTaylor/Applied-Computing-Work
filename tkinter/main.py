import tkinter

# GUI with a label and a button


def main():
    root = tkinter.Tk()
    root.title("Hello World!")
    root.geometry("400x300")  # Set the window size to 400x300
    label = tkinter.Label(root, text="Hello World!")
    label.pack()
    quit_button = tkinter.Button(root, text="Quit", command=root.quit)
    quit_button.pack()
    root.mainloop()


# Call the main function to display the window
main()
