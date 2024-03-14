# lab7.2.2-writeNumber.py
# Program that writes a number to a file. Program creates a file called count.txt and writes a number to it.
# author: Tomasz Uszynski

FILENAME = "count.txt"                      # Define the file name.

def writeNumber(number):                    # Define function to write the number to the file.
    with open(FILENAME, "wt") as f:         # Open file for writing text.
    # write takes a string so we need to convert
        f.write(str(number))                # Write the number to the file.
# test it
writeNumber(12)                              # Call the function and pass the number 12 to it.