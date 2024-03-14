# lab7.5-menu.py
# Program with a menu system with add, view, save and quit options. Just show menu and options. Define functions to add, 
# view and save students.
# author: Tomasz Uszynski

from doSave import doSave                    # Import the doSave function from the doSave module.
students= []                                # Create an empty list to store students data.
def displayMenu():                          # Function to display menu.

    print("what would you like to do?")     # Print menu.
    print("\t(a) Add new student")          # Print add option.
    print("\t(v) View students")            # Print view option.
    print("\t(s) Save students")            # Print save option.
    print("\t(q) Quit")                     # Print quit option.
    choice = input("type one letter (a/v/s/q):").strip()    # Ask user to select an option.
    return choice                           # Return user's choice.

def doAdd(students):                        # Function to add students.
 # Future functionality
    print("in adding")                      # Print adding.   
def doView(students):                       # Function to view students.
 # Future functionality
    print("in viewing")                     # Print viewing.
def doSave(students):                       # Function to save students data.
# Future functionality
    print("in save")                        # Print saving.


choice = displayMenu()                      # Call the function and store the result in a variable.
while(choice != 'q'):                       # While user's choice is not q.
    if choice == 'a':                       # If user's choice is a.
        doAdd(students)                     # Call doAdd function.
    elif choice == 'v':                     # If user's choice is v.
        doView(students)                    # Call doView function.
    elif choice == 's':                     # If user's choice is s.
        doSave(students)                    # Call doSave function.
    elif choice !='q':                      # If user's choice is not q.
        print("\n\nPlease select either a,v,s or q")    # Print message.
    choice=displayMenu()                    # Call the function and store the result in a variable.