# useFib.py
# This program prompts the user for a number and prints out the fibonacci sequence of that many numbers. 
# This is done by importing the fibonacci function from myFunctions.py.
# ORIGINALLY WRITTEN BY ANDREW BEATTY, and modified by Tomasz Uszynski
# author: Tomasz Uszynski         

import myFunctions                                      # Import myFunctions module.
while True:                                             # Infinite loop.
    try:
        nTimes = int(input("How many?: "))              # Prompt the user for a number and store it in nTimes.
        if nTimes < 0:                                  # If nTimes is less than 0.
            print("You must enter a positive integer.") # Print "You must enter a positive integer."
            continue                                    # Continue to the next iteration of the loop.
    except ValueError:                                  # If a ValueError is raised.
        print("You must enter an integer value.")       # Print "You must enter an integer value".
        continue                                        # Continue to the next iteration of the loop.
   
    print(myFunctions.fibonacci(nTimes))                # Print the fibonacci sequence of nTimes numbers.
    break                                               # Break out of the loop.