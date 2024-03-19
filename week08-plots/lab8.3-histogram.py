# lab8.3-histogram.py
# Program that plots a histogram of the salaries from Question 1. The histogram should have 10 bins.
# author: Tomasz Uszynski

import numpy as np                    # Library that we will use to generate random numbers.  
import matplotlib.pyplot as plt       # Import the matplotlib library.

minSalary = 20000                     # Minimum salary that can be generated.
maxSalary = 80000                     # Maximum salary that can be generated.
numberOfEntries = 10                  # Number of salaries that will be generated.

np.random.seed(1)                     # Modified to ensure that the same random numbers are generated each time the program is run.
                                      # Useful for testing and debugging.
                                      
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries) # Function that generates the random salaries.

plt.hist(salaries)                    # Create the histogram.
plt.show()                            # Display the histogram.