cd# lab4.1.1-isEven.py
# Program asks the user to enter in a number, and the program will tell the user if the number is even or odd.
# author: Tomasz Uszynski

number = int(input("enter a number: "))            # Reads in input and store as value number.

if (number % 2) == 0:                              # Checks if the remainder of dividing the variable number by 2 is equal to 0.
   print(f"Number {number} is even number.")       # If True prints out if print result.
else:                                              
   print(f"Number {number} is odd number.")        # If False prints out else print result.