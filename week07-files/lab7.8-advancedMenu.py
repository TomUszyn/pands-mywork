# lab7.8-advancedMenu.py
# Program with advanced menu system with add, view, save, load and quit options.
# author: Tomasz Uszynski
#   
import json                                     # Import json module.

FILENAME = "storedata.json"                     # Set the file name to store data.        

students = []                                   # Create an empty list to store students data.

def displayMenu():                              # Function to display menu.
    print("Make a Choice: ")                    # Print menu.
    print("\tType (a) to add")                  # Print add option.
    print("\tType (v) to view")                 # Print view option.
    print("\tType (s) to save")                 # Print save option.
    print("\tType (l) to load")                 # Print load option.
    print("\tType (q) to quit")                 # Print quit option.
    choice = input("Please select (a/v/s/l/q): ")  # Ask user to select an option.
    return choice                               # Return user's choice.


def getModules():                               # Function to get modules.
    modules = []                                # Create an empty list to store modules.
    modulename = str.capitalize(input("Please enter the module name (Leave blank to quit): ")) # Ask user to enter module name.
    while modulename != "":                     # While module name is not empty.
        module = {}                             # Create an empty dictionary to store module data.
        module["name"] = modulename             # Set module name.
        module["grade"] = input(f"Please enter the grade for {modulename}: ") # Ask user to enter grade for module.
        modules.append(module)                  # Append module to the list.
        modulename = input("Please enter the module name (Leave blank to quit): ") # Ask user to enter module name.
    return modules                              # Return modules list.


def doAdd(students):                            # Function to add students.
    student ={}                                 # Create an empty dictionary to store student data.
    student["name"] = str.capitalize(input("Please enter name: "))  # Ask user to enter student name.
    student["modules"] = getModules()           # Get modules for student.
    students.append(student)                    # Append student to the list.
    return students                             # Return students list.

    
def doView(students):                           # Function to view students.
    for student in students:                    # For each student in students list.
        print (student["name"])                 # Print student name.
        for module in student["modules"]:       # For each module in student modules.
            print ("\t", module["name"], "\t:", module["grade"]) # Print module name and grade.
    return students                             # Return students list.


def doSave(students):                           # Function to save students data.
    with open(FILENAME, "wt") as f:             # Open file to write data.
        json.dump(students, f)                  # Write students data to the file.
    print("Student data are stored.")           # Print saved.
    return students                             # Return students list.


def doLoad(students):                           # Function to load students data.
    print("Data are loaded.")                   # Print loaded.
    with open (FILENAME, "rt") as f:            # Open file to read data.
        return json.load(f)                     # Return loaded data.


menuChoice = {                                  # Create a dictionary with menu options.
    'a': doAdd,                                 # Add option.
    'v': doView,                                # View option.
    's': doSave,                                # Save option.
    'l': doLoad                                 # Load option.   
}                                               # End of dictionary.

choice = displayMenu()                          # Call displayMenu function and store the result in choice variable.
while choice != "q":                            # While choice is not q.
    if choice in menuChoice:                    # If choice is in menuChoice dictionary.
        students = menuChoice[choice](students) # Call function from menuChoice dictionary and pass students list.
    else:                                       # If choice is not in menuChoice dictionary.   
        print ("Invalid choice. Please try again.") # Print invalid choice.

    choice = displayMenu()                      # Call displayMenu function and store the result in choice variable.

print ("Goodbye!")                              # Print goodbye when user selects q option.