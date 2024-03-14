# lab7.4-readJSON.py
# Program that reads a dictionary from a file using the json module. Program reads a file called testdict.json 
# and prints the dictionary. Program uses the readDict function to read the dictionary from the file. 
# If the file does not exist, readDict will throw an error.
# author: Tomasz Uszynski

import json                                              # Import json module.

FILENAME ="testdict.json"                                # Define the file name.

def readDict():                                          # Define function to read the dictionary from the file.
   with open(FILENAME) as f:                             # Open file for reading text.
         return json.load(f)                             # Read the dictionary from the file and return it.

somedict = readDict()                                    # Test the function by calling it and storing the result in a variable.
print(somedict)                                          # Print the dictionary.