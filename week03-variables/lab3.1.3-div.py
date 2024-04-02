# lab3.1.3-div.py
# Program that reads in two numbers and divides the first one by the second and give the integer result and the remainder.
# author: Tomasz Uszynski

x = int(input("Enter first number: "))                        # int() converts input value to integer.
y = int(input("Enter the number you want to divide by: "))    # Now we can do mathematical operations.

answer = int(x // y)                                          # It divides x by y and rounds down to the nearest integer.
remainder =x % y                                              # Counts remainder.

print("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))  # Prints out result.