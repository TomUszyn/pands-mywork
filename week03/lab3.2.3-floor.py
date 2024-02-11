# lab3.2.3-floor.py
# Program, that takes in a float and outputs an int rounded down.
# author: Tomasz Uszynski

import math                                                     # Imports the module math.

numberTofloor = float(input("Enter a float number: "))          # Converts numeric input value to float.
flooredNumber = math.floor(numberTofloor)                       # Computes the largest integer less than or equal 
                                                                # to numberTofloor.

print('{} floored is {}'.format(numberTofloor, flooredNumber))  # Prints out result.