# lab6-doAdd.py
# Function doAdd() is called and it is adding students and related modules and grades to the list.
# author: Tomasz Uszynski

students = []                                       # list students
def readModules():                                  # function readModules
    return []                                       # return st
def doAdd(students):                                # function doAdd
    currentStudent = {}                             # dictionary currentStudent
    currentStudent["name"] = input("enter name: ")  # input statement and assign value to key name in dictionary currentStudent
    currentStudent["modules"] = readModules ()      # assigns result of readModule to currentStudent["modules"]
    students.append(currentStudent)                 # append currentStudent to students

def readModules():                                  # function readModules
    modules = []                                    # list modules
    moduleName = input("\tEnter the first Module name (blank to quit):").strip()    # input statement
    
    while moduleName != "":                         # while loop 
        module = {}                                 # dictionary module 
        module["name"] = moduleName                 # assign value of moduleName to key name in dictionary module
        # we are not doing error handling
        module["grade"] = int(input("\t\tEnter grade:")) # input statement and assign value to key grade in dictionary module
        modules.append(module)                      # append module to modules
        # now read the module name
        moduleName = input("\tEnter next module name (blank to quit):").strip()   # input statement
        
    return modules                                  # return statement

#test

doAdd(students)                                     # function doAdd called     
doAdd(students)                                     # function doAdd called
print(students)                                     # print statement