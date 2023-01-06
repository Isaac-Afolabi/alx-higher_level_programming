#!/usr/bin/python3
if __name__ == "__main__":
    # Import the add function from the add_0 module
    add_0 = __import__("add_0")
    add = add_0.add

    # Define the variables a and b
    a = 1
    b = 2

    # Call the add function and print the result
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))

