# lab3.1.2-sub.py
# Program that reads in two numbers and subtracts the first one from the second one.
# author: Tomasz Uszynski

x = int(input("Enter first number: "))              # int() converts input value to integer and store as value x.
y = int(input("Enter second number: "))             # int() converts input value to integer and store as value y
                                                    # Now we can do mathematical operations.                                                 
answer = x - y                                       # Substract result stored as answer.

print("{} minus {} is {}".format(x, y, answer))     # Prints our formated result.

# We will have Syntax Error (ValueError: invalid literal for int() with base 10:) if we will try input data than integer.