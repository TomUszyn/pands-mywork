# lab4.1.2-grade.py
# Program reads in a student’s percentage mark and prints out corresponding the grade.
# author: Tomasz Uszynski

percentage = float(input("Enter the percetage: "))     # Enter float number.

roundedNumber = round(percentage)

if roundedNumber < 0 or roundedNumber > 100:           # Checks if we are inside expected range.
    print("Please enter a number between 0 and 100")   # If not inform to use correct number.
elif roundedNumber < 40:                               # Range between 0 and 39.
    print("Fail")                                      # Prints out Fail.
elif roundedNumber < 50:                               # Range between 40 and 49.
    print("Pass")                                      # Prints out Pass.
elif roundedNumber < 60:                               # Range between 50 and 59.
    print("Merit 2")                                   # Prints out Merit 2.
elif roundedNumber < 70:                               # Range between 60 and 69.
    print("Merit 1")                                   # Prints out Merit 1. 
else:                                                  # Range betwwen 70 and 100.
    print("Distinction")                               # Prints out Distiction. 