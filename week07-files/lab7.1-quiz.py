# lab7.1-quiz.py
# author: Tomasz Uszynski

# To check funcionalities this file user need to run section one by one. 
# When finish first section, user can comment out the first section and 
# run the second section and so on.


# a. What will happen when the program runs and the file is not exist?

with open('test-a.txt',) as f:
    data = f.read()
    print(data)
    
# answer: The program will display an error message and stop running.
# The error message will be: FileNotFoundError: [Errno 2] No such file or directory: 'test-a.txt'

# b. Look at the program below, if the file test-b.txt does not exist, what will be outputted to 
# the console when the program is run?

#with open('test-b.txt', 'w') as f:  # Open file for writing text.
#    data = f.write("test b\n")      # Write data to file.    
#    print(data)                     # Print the number of characters written to the file.
#    
#with open('test-b.txt', 'w') as f2: # Open file for writing text.
#    data = f2.write("another line\n")   # Write data to file.
#    print(data)                     # Print the number of characters written to the file.
    
# answer: The program will display the number of characters written to the file. In this case, 
# the number of characters written to the file will be 7 and 13.

# c. What will the contesnts of the file test-b.txt be when this program is run?

# answer: The contents of the file test-b.txt will be:
# another line (without the quotes) because the second write operation will overwrite 
# the first write operation.


# d. Look at the modified program below, what will the contents of the file be after this program is run?

#with open('test-d.txt', 'w') as f:  # Open file for writing text. w mode will overwrite the file.
#    data = f.write("test d\n")      # Write data to file. Returns the number of characters written to the file.    
#    print(data)                     # Print the number of characters written to the file. 
#    
#with open('test-d.txt', 'a') as f2: # Open file for writing text. a mode will append to the file.
#    data = f2.write("another line\n")   # Write data to file. Returns the number of characters written to the file.
#    print(data)                     # Print the number of characters written to the file.
#    
# answer: The contents of the file test-d.txt will be:
# test d                (without the quotes) on one line
# another line          (without the quotes) on the next line