# lab4.2.5-topthree.py
# Program generates 10 random numbers (0-100),prints them out then prints out the top three.
# author: Tomasz Uszynski


import random               # Imports module.

howMany = 10                #    
rangeFrom = 0               # Declared values.
rangeTo = 100               #    
topHowmany = 3              #

numbers = []                # Creates empty list.

# It uses the 'random' module to create `howMany` random numbers between `rangeFrom` and `rangeTo`.
# for loop iterates howMany times, where howMany is a variable that specifies the desired 
# number of random numbers to generate.
# random.randint(rangeFrom, rangeTo) function generates a random integer between rangeFrom and rangeTo.
# Each randomly generated number is appended to the numbers list.
# After the loop completes, the code prints a formatted string using an f-string. 
# It displays the total count of random numbers (howMany) and the list of those numbers (numbers).

for i in range(0,howMany):
    numbers.append(random.randint(rangeFrom,rangeTo))
print(f"{howMany} random numbers:\t{numbers}")

# Code creating a new list called topOnes and copying the contents of the numbers list into it using the .copy() method.
# the topOnes list is sorted in descending order using the .sort(reverse=True) method. This means that the largest
# numbers will appear at the beginning of the list.
# Prints a formatted message and displays the top topHowmany numbers from the topOnes list.

topOnes = numbers.copy()
topOnes.sort(reverse=True)
print(f"The top {topHowmany} are \t\t{topOnes[0:topHowmany]}")