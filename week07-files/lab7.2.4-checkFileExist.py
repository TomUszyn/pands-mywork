# lab7.2.4-checkFileExist.py
# Program that checks if a file exists. If it does not exist, the program will create it.
# author: Tomasz Uszynski

import os.path                      # Import os.path module.

FILENAME = "count.txt"              # Define the file name.

if not os.path.isfile(FILENAME):    # Check if the file exists.           
    print ("File does not exist")   # Print message if file does not exist.
    
