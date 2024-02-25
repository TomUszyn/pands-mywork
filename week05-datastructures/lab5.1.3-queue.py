# lab5.1.3-queue.py
# Create a program that puts 10 random numbers into a queue(list), the program should then output all the values 
# in the queue, then take the numbers from the queue one at a time, print it and the current numbers still 
# in the queue. (the command pop(0) takes the first element out of a list)
# author: Tomasz Uszynski

import random                                       # Imports module.
queue = []                                          # Creates empty list.
numberOfNumbers=10                                  # Number of numbers.
rangeTo=100                                         # Range.

for n in range(0,numberOfNumbers):                  # Generates and appends random numbers to queue.
      queue.append(random.randint(0,rangeTo))

print (f"Queue is {queue}.")                         # Prints out contents of queue

while len(queue) != 0:                              # Sets condition.

    currentNumber = queue.pop(0)                    # Takes numbers from queue until will be empty.
    # print ("Current Number is {currentNumber} and the queue is {queue} ") # Missing f-string.
    print (f"Current Number is {currentNumber} and the queue is {queue}. ")  # Prints out results of each step.

print ("The queue is now empty.")                    # Prints out sentence.

# Source of code is Lab 05 DataStructures.pdf by Andrew Beatty. 
# Usefull information about F-string on the website: https://realpython.com/python-f-strings/
