from tkinter import *


def main():
    """the main function for the UI of the todo list application."""
    root = Tk()
    root.title("Todo")
    root.geometry("800x600")

    # Create a label for the todo list
    label = Label(root, text="Todo List")
    label.pack()

    # Create a listbox to display the todo items
    listbox = Listbox(root)
    listbox.pack()

    # Create an entry field for adding new todo items
    entry = Entry(root)
    entry.pack()

    # Create a button to add new todo items
    def add_todo():
        todo = entry.get()
        if todo:
            listbox.insert(END, todo)
            entry.delete(0, END)

    add_button = Button(root, text="Add", command=add_todo)
    add_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
