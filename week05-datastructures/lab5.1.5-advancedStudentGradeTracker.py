# lab5.1.5-advancedStudentGradeTracker.py
# Program that will read in the data for the data structure above, ie reads in a student’s name, 
# then keeps reading in their modules and grades (until the user enters a blank module name).
# author: Tomasz Uszynski

student = {}                                                                 # Creates empty dict student.
student["name"] = str.capitalize(input("Enter name of student: "))           # Adds input data to the dictionary
                                                                             # in format "name" : student

student["modules"] = []                                                      # Adds empty list "modules" to the dict.

while True:                                                                  # Loop runs until the user enters a blank course name.
    courseName = str.capitalize(input("Enter name of the course (or leave blank to finish): "))
    if not courseName:                                                       # If the course name is blank, exit the loop.
        break                                                                
    grade = int(input("Enter student grade: "))                              # Asks about grade if entered course name.
    student["modules"].append({"courseName": courseName, "grade": grade})    # Adds a new course and grade to the student modules list.
    
print("Student: {}".format(student["name"]))                                 # Prints out student name.

for module in student["modules"]:
    print(f'\t{module["courseName"]:<20} : {module["grade"]:>2}')            # Prints out couses names and related grades. 

# To format print of modules we are using align to left :<20 and align ringt :>2. More details on the website: https://fstring.help/
# https://realpython.com/python-for-loop/ Explains about for loop.
# https://realpython.com/python-while-loop/ Explains about while loop.           
