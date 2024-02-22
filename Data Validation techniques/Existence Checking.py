# Write a script that checks whether a variable is defined or not and handles both scenarios appropriately.
x = 10


def is_var_defined(var):
    if var in locals() or var in globals():
        print("Variable is defined")
    else:
        print("Variable is not defined")


is_var_defined("x")  # Variable is defined
is_var_defined("y")  # Variable is not defined
