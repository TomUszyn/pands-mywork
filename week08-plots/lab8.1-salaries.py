# lab8.1-salaries.py
# This program generates a list of random salaries. The number of salaries and the range of salaries can be adjusted as needed.
# The range of salaries is set between 20000 and 80000. The number of salaries in the list can be adjusted as needed.
# The purpose of this program is to demonstrate how to generate random salaries and store them in a list for further processing or analysis.
# It is a good idea to have your absolute values set into varialbes at the beginning of your program such as minSalary and maxSalary.
# This way, if you need to change the range of salaries, you can do so easily by changing the values of the variables. We declare the numberOfEntries
# author: Tomasz Uszynski

import numpy as np  # Library that we will use to generate random numbers. 


minSalary = 20000   # Minimum salary that can be generated         
maxSalary = 80000   # Maximum salary that can be generated      
numberOfEntries = 10    # Number of salaries that will be generated



np.random.seed(1)   # Modified to ensure that the same random numbers are generated each time the program is run.
                    # Useful for testing and debugging.
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries) # Function that generates the random salaries.
print(salaries)     # Prints the list of random salaries.



salariesPlus = salaries + 5000  # Adds 5000 to each salary in the list.
print(salariesPlus) # Prints the list of salaries with a 5000 increase.


salariesMult = salaries * 1.05  # Multiplies each salary in the list by 1.05.
print(salariesMult) # Prints the list of salaries with a 5% increase.
newSalaries = salariesMult.astype(int) # Converts the list of salaries to integers.
print(newSalaries) # Prints the list of salaries as integers.