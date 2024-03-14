# lab7.3.1-writeJSON.py
# Program that writes a dictionary to a file using the json module.
# author: Tomasz Uszynski

import json                                             # Import json module.
FILENAME="testdict.json"                                # Define the file name.
sample= dict(name='Adam', age=34, grades=[15,45,59])    # Define a sample dictionary.
def writeDict(obj):                                     # Define function to write the dictionary to the file.
    with open(FILENAME, 'wt') as f:                     # Open file for writing text.
        json.dump(obj,f)                                # Write the dictionary to the file.

writeDict(sample)                                       # Test the function by calling it and passing the sample dictionary to it.                                  