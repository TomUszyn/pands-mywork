# doLoad.py Part of lab7
# Function doLoad() is defined to read the data from the file storedata.json. 
# The file is opened in read text mode and the data is loaded using the json.load() function. 
# The data is then returned to the calling function. The function is called and the data is printed to the console. 
# The data is then stored in the variable students. The variable students is then printed to the console.
# author: Tomasz Uszynski

import json                             # Import the json module.

FILENAME ="storedata.json"              # Define the file name.

def doLoad():                           # Define function to load the data from the file.
    print("in do load")                 # Print message.
    with open (FILENAME, "rt") as f:    # Open file for reading text.
        return json.load(f)             # Load the data from the file and return it.
    
students = doLoad()                     # Call the function and store the result in a variable.
print(students)                         # Print the data to the console.       