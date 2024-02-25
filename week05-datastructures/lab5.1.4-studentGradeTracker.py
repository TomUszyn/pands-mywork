# lab5.1.4-studentGradetracer.py
# Program that stores a student name and a list of her courses and grades in a dict, 
# the program should then print out her data. The number of course she has could change.
# author: Tomasz Uszynski

student = {}                                                                # Creates empty dict student.
student["name"] = str.capitalize(input("Enter name of student: "))          # Adds input data to the dictionary
                                                                            # in format "name" : student
numberOfCourses = int(input("How many courses does the student attend?: ")) # Declares quantuty of courses.

student["modules"] = []                                                     # Adds empty list "modules" to the dict.

for i in range(numberOfCourses):                                            # for loop collects data such as name of course and grade.
    courseName = str.capitalize(input("Enter name of the course: "))
    grade = int(input("Enter student grade: "))
    student["modules"].append({"courseName": courseName, "grade": grade})   # Adds a new course and grade to the student modules list.

print("Student: {}".format(student["name"]))                                # Prints out student name.

for module in student["modules"]:
    print(f'\t{module["courseName"]:<20} : {module["grade"]:>2}')           # Prints out couses names and related grades.

# To format print of modules we are using align to left :<20 and align ringt :>2. More details on the website: https://fstring.help/
# https://realpython.com/python-for-loop/ Explains about for loop.