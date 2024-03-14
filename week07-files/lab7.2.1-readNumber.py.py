# lab7.2.1-readNumber.py
# Program that reads a number from a file and prints it.
# To test it we need to create a file called count.txt and put a number in it.
# author: Tomasz Uszynski

FILENAME = "count.txt"                      # Define the file name.

def readNumber():                           # Define function to read the number from the file.
    with open(FILENAME) as f:               # Open file for reading text.
        number = int(f.read())              # Read the number from the file and convert it to an integer.
        return number                       # Return the number.
# test it
num = readNumber()                          # Call the function and store the result in a variable.
print (num)                                 # Print the number.