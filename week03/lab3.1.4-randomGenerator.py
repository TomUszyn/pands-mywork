# lab3.1.4-randomGenerator.py
# Program that prints out a random number between 1 and 10.
# author: Tomasz Uszynski

import random                                              # Imports the module random

first_number = int(input("Enter first number of range: ")) # int() converts input value to integer and store as first_number.
last_number = int(input("Enter last number of range: "))   # int() converts input value to integer and store as last_number.

number = random.randint(first_number, last_number)         # Generate random number from user inputs range including those numbers.

print("Here is a random number {}".format(number))         # Prints out result.