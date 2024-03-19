# lab8.4-scatter.py
# Program that makes a list called ages that has same number random values as salaries, (range:21 to 65)
# Make a scatter plot of this data.
# author: Tomasz Uszynski

import numpy as np                    # Library that we will use to generate random numbers.  
import matplotlib.pyplot as plt       # Import the matplotlib library.

minSalary = 20000                     # Minimum salary that can be generated.
maxSalary = 80000                     # Maximum salary that can be generated.
numberOfEntries = 10                  # Number of salaries that will be generated.
minAge = 21                           # Minimum age that can be generated.
maxAge = 65                           # Maximum age that can be generated.


np.random.seed(1)                     # Modified to ensure that the same random numbers are generated each time the program is run.
                                      # Useful for testing and debugging.
                                      
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries) # Function that generates the random salaries.
ages = np.random.randint(minAge, maxAge, numberOfEntries) # Function that generates the random ages.

plt.scatter(ages, salaries)           # Create the scatter plot.

xpoints = np.array(range(1, 101))     # Create an array of x values from 1 to 100.
ypoints = xpoints * xpoints           # Create an array of y values that are the square of the x values.

plt.plot(xpoints, ypoints, color = 'r') # Create the plot.

plt.title('Random salaries and ages') # Add a title to the scatter plot.
plt.xlabel('Salaries')                # Add a label to the x-axis.
plt.ylabel('Age')                     # Add a label to the y-axis. 
plt.legend(['y = x^2', 'salaries'])   # Add a legend to the plot.       
plt.show()                            # Display the histogram.

plt.savefig('prettier-plot.png')      # Save the plot to a file.