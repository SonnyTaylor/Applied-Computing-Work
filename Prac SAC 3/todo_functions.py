import csv

class TodoList:
    def __init__(self, csv_file):
        self.todo_items = self.get_todo_items_from_csv(csv_file)

    def get_todo_items_from_csv(self, csv_file):
        """Return a list of todo items from a CSV file."""
        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            todo_items = list(reader)
        return todo_items

    def add_todo_item(self, todo):
        """Add a new todo item to the list of todo items."""
        self.todo_items.append(todo)

    def remove_todo_item(self, todo):
        """Remove a todo item from the list of todo items."""
        self.todo_items.remove(todo)

    def get_todo_items(self):
        """Return the list of todo items."""
        return self.todo_items


todo_list = TodoList("todo.csv")
