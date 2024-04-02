# lab3.1.5-randomFruit.py
# Program that prints out random Fruit.
# author: Tomasz Uszynski

import random                                      # Import module random.

fruits = ['Apple', 'Orange', 'Banana' ,'Pear']     # Create list with four elements.

index = random.randint(0, len(fruits)-1)           # Produce a random integer between 0 and the highest valid index of the fruits list 
                                                   # and store it as index.

fruit = fruits[index]                              # Pick element related to index.

print("A random fruit is {}.".format(fruit))       # Print out result.