# lab7.2.3-countProgramRuns.py
# Write a program that counts how many times it was run.
# For this exercise will have to store data outside of memory, and that is accessible
# each time the program is run, (persistent data). We would normally use a
# database for something like this, but we can use a file.
# To make life easier let’s assume that the file already exists. So, we can just read
# the current count from it then overwrite it with the new count.
# Create a file called count.txt and put in 0 into it
# author: Tomasz Uszynski

import os.path                                      # Import the os.path module.

FILENAME = "count.txt"                              # Define the file name.

def writeNumber(number):                            # Define function to write the number to the file.
    with open(FILENAME, "wt") as f:                 # Open file for writing text.
    # write takes a string so we need to convert
        f.write(str(number))                        # Write the number to the file.
        
if not os.path.isfile(FILENAME):                    # Check if file does not exist.
    print ("File does not exist")                   # Print message if file does not exist.
    #initialise file here
    writeNumber(0)                                  # Create the file and write 0 to it.

def readNumber():                                   # Define function to read the number from the file.
    with open(FILENAME) as f:                       # Open file for reading text.
        number = int(f.read())                      # Read the number from the file and convert it to an integer.
        return number                               # Return the number.

# Main program
 
num = readNumber()                                  # Call the function and store the result in a variable.
num += 1                                            # Increment the number.
print (f"We have run this program {num} times")     # Print the number.
writeNumber(num)                                    # Call the function and pass the number to it.