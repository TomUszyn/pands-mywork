# lab8.2-plot.py
# Program that plots the function y = x^2. Simple code to demonstrate the use of the matplotlib library.
# author: Tomasz Uszynski

import matplotlib.pyplot as plt         # Import the matplotlib library.
import numpy as np                      # Import the numpy library.

xpoints = np.array(range(1, 101))       # Create an array of x values from 1 to 100.
ypoints = xpoints * xpoints             # Create an array of y values that are the square of the x values.

plt.plot(xpoints, ypoints)              # Create the plot.
plt.show()                              # Display the plot.