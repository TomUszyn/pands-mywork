# lab8.5-bar.py
# Program that makes a list of five counties and plots pie plot of unique occurrences of values in an array.
# Program demonstrates more than just how to plot a pie plots in this.
# author: Tomasz Uszynski

import numpy as np                    # Library that we will use to generate random numbers.
import matplotlib.pyplot as plt       # Import the matplotlib library.

possibleCounties = ['Kerry', 'Dublin', 'Galway', 'Cork', 'Limerick'] # List of counties.

counties = np.random.choice(possibleCounties, p=[0.1, 0.3, 0.2, 0.12, 0.28], size=(100)) # Function that generates the random counties.

unique, counts = np.unique(counties, return_counts=True) # Function that returns the unique values and their counts.

plt.pie(counts, labels = unique)       # Create the pie plot.
plt.show()                             # Display the pie plot.