# lab3.2.4-convert.py
# Program, that takes in a float amount of dollars and returns that absolute amount in cent.
# author: Tomasz Uszynski

amountInDollars = float(input("Please enter an amount: "))      # Converts numeric input value to float.
abs_amount = abs(amountInDollars)                               # Returns absolute value of previous input.
amountInCents = int(abs_amount * 100)                           # Coverts dollars to Cents.
print("That amount in cents is {}".format(amountInCents))       # Prints out result.