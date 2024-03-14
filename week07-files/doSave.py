# doSave.py Part of lab7
# The doSave() function is defined to save the data to the file storedata.json.
# The file is opened in write text mode and the data is saved using the json.dump() function.
# The function is called and the data is printed to the console.
# The data is then stored in the variable students.
# author: Tomasz Uszynski

import json                                     # Import the json module.

FILENAME ="storeadddata.json"                   # Define the file name.

def doSave(students):                           # Function to save students data.
    with open(FILENAME, "wt") as f:             # Open file to write data.
        json.dump(students, f)                  # Write students data to the file.
    print("Student data are stored.")           # Print saved.
    return students                             # Return students list.