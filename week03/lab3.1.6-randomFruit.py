# lab3.1.6-randomFruit.py
# Program that prints out random Fruit.
# author: Tomasz Uszynski

import random                                      # Imports module random.

fruits = ('Apple', 'Orange', 'Banana' ,'Pear')     # Creates tuple with four elements.

index = random.randint(0, len(fruits)-1)           # Produces a random integer between 0 and the highest valid index of the fruits list 
                                                   # and store it as index.

fruit = fruits[index]                              # Picks element related to index.

print("A random fruit is {}.".format(fruit))       # Prints out result.