# lab3.2.1-round,py
# Program rounds a number
# Be careful of round, it rounds to the nearest even number. Do not use if accuracy is essential.
# author: Tomasz Uszynski.

numberToRound = float(input("Enter a float number: "))
roundedNumber = round(numberToRound)
print('{} rounded is {}.'.format(numberToRound, roundedNumber))