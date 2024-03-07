# la6-finalMenu.py
# This is advanced menu system that allows the user to add new students with related data, 
# view students and related data and quit the program.
# author: Tomasz Uszynski


def displayMenu():                              # function displayMenu
    print("What would you like to do?")         # 
    print("\t(a) Add new student")              # print statements
    print("\t(v) View students")                #
    print("\t(q) Quit")                         #
    choice = input("Type one letter (a/v/q):").strip()  # input statement
    return choice                               # return choice

def doAdd(students):                                # function doAdd
    currentStudent = {}                             # dictionary currentStudent
    currentStudent["name"]=input("Enter name :")    # input statement
    currentStudent["modules"]= readModules()        # assigns result of readModule to currentStudent["modules"]
    students.append(currentStudent)                 # append currentStudent to students
    
def readModules():                                  # function readModules
    modules = []                                    # list modules
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()   # input statement
    while moduleName != "":                         # while loop
        module = {}                                 # dictionary module
        module["name"]= moduleName                  # assign value of moduleName to  key name in dictionary module
    # We are not doing error handling
        module["grade"]=int(input("\t\tEnter grade:")) # input statement and assign value to key grade in dictionary module
        modules.append(module)                         # append module to modules
    # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit) :").strip()    # input statement
    return modules                                      # return statement

def displayModules(modules):                                # function displayModules
    print ("\tName \tGrade")                                # print statement
    for module in modules:                                  # for loop
        print(f"\t{ module['name']} \t{ module['grade']}")  # print statement
        
def doView(students):                                       # function doView
    for currentStudent in students:                         # for loop
        print(currentStudent["name"])                       # print statement
        displayModules(currentStudent["modules"])           # function displayModules called

#main program
students = []                                               # list students
choice = displayMenu()                                      # assign result of function to  variable choice
while(choice != 'q'):                                       # while loop
 # we could do this with lamda functions
 # will be basic for the moment
    if choice == 'a':                                       # if statement
        doAdd(students)                                     # function doAdd called
    elif choice == 'v':                                     # elif statement
        doView(students)                                    # function doView called
    elif choice !='q':                                      # elif statement
        print("\n\nplease select either a,v or q")          # print statement
    choice=displayMenu()                                    # assign result of  function to variable choice