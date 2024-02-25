# lab5.1.5-advancedStudentGradeTracker.py
# Program that will read in the data for the data structure above, ie reads in a student’s name, 
# then keeps reading in their modules and grades (until the user enters a blank module name). Multiple student version.
# author: Tomasz Uszynski

import webbrowser

students = {}                                                                         # Creates empty dict students.

while True:                                                                           # Loop runs until the user enters a blank student name.
    student = {}
    studentName = input("Enter name of student (or leave blank to finish): ")
    if not studentName:                                                                # If the student name is blank, exit the loop.
        break
    student["name"] = str.capitalize(studentName)                                      # Adds input data to the dictionary
                                                                                      # in format "name" : student.

    student["modules"] = []                                                  # Student dictionary with empty list associated with key "modules".
    while True:                                                                       # Loop runs until the user enters a blank course name.
        courseName = str.capitalize(input("Enter name of the course (or leave blank to finish): "))
        if not courseName:                                                            # If the course name is blank, exit the loop.
            break
        grade = int(input("Enter student grade: "))                                   # Asks about grade if entered course name.
        student["modules"].append({"courseName": courseName, "grade": grade})         # Adds a new course and grade to the student modules list.

    students[student["name"]] = student                                         # The key for this entry is the value of student["name"], 
                                                                                # and the corresponding value is the entire student dictionary.

for studentName, student in students.items():                                   #  
    print(f"Student: {studentName}")                                            # Prints all students names stored in the students dictionary
    for module in student["modules"]:                                           # along with their respective module names and grades.
        print(f"\t{module['courseName']:<20} : {module['grade']:>2}")           #

# To format print of modules we are using align to left :<20 and align ringt :>2. More details on the website: https://fstring.help/
# Base souce code taken from: Lab 05 dataStructures.pdf
# webbrowser.open("https://realpython.com/python-for-loop/") Explains about for loop.
# webbrowser.open("https://realpython.com/python-while-loop/") Explains about while loop.           