# useFib.py
# This program prompts the user for a number and prints out the fibonacci sequence of that many numbers. 
# This is done by importing the fibonacci function from myFunctions.py.
# ORIGINALLY WRITTEN BY ANDREW BEATTY, and modified by Tomasz Uszynski
# author: Tomasz Uszynski         

import myFunctions                                  # Import myFunctions module.
try:
    nTimes = int(input("How many?: "))               # Prompt the user for a number and store it in nTimes.
except ValueError:                                  # If a ValueError is raised.
    print("You must enter an integer value.")        # Print "You must enter an integer value".
    nTimes = int(input("How many?: "))               # Prompt the user for a number and store it in nTimes.

print(myFunctions.fibonacci(nTimes))                # Print the fibonacci sequence of nTimes numbers.