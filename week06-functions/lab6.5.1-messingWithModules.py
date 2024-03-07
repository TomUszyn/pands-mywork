# lab6.5.1-messingWithModules.py
# anaconda has installed a lot of modules already onto 
# author: Tomasz Uszynski


from constraint import *                   # import everything from the constraint module.
from github import Github                  # import the Github class from the github module.
import nltk                                # import the nltk module.

import math as m                           # import the math module and call it m.

#from math import cos                      # import the cos function from the math module.

var = m.cos(3.14)                          # call the cos function from the math module.

print(var)                                 # print the result.