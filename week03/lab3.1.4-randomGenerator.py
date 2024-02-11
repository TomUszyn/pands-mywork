# lab3.1.4-randomGenerator.py
# Program that prints out a random number between 1 and 10.
# author: Tomasz Uszynski

import random                                              # Imports the module random

number = random.randint(1, 10)                             # Generates random number from range 1 to 10 including those numbers. 

print("Here is a random number {}".format(number))         # Prints out result.