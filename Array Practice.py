grocery_list = ["Apples", "Milk", "Pasta", "Bread", "Eggs"]

# First item in the array wich would be "Apples"
first_item = grocery_list[0]
print(first_item)

# Get input for what to add to the list and append it
grocery_list_input = input("What do you want to add to the list? ")
grocery_list.append(grocery_list_input)
print(grocery_list)

#  Get input for what to remove from the list
remove_from_list = input("What do you want to remove from the list? ")
grocery_list.remove(remove_from_list)
print(grocery_list)

# Sort the list in alphabetical order and print it
grocery_list.sort()

print("this is the sorted grocerylist:", grocery_list)
