# myFunctions.py
# This program is to show how to make a module, that contains functions, and test cases for the functions
# it has a function called fibonacci that takes in number and returns a list containing a fibonacci squence with that 
# many numbers.
# Program is orginally written by Andew Beatty.
# author: Tomasz Uszynski



import logging                                      # Import logging module.
# logging.basicConfig(level=logging.DEBUG)          # Set logging level to DEBUG. Commented out to prevent debug messages from being printed.

def fibonacci(number):                              # Define function fibonacci that takes in number.         
    if number < 0:                                  # If number is less than 0.
        raise ValueError("number must be > 0")      # Raise ValueError with message "number must be > 0".
    if number == 0:                                 # If number is equal to 0.
        return []                                   # Return an empty list.
    
    a = 0                                           # Set a to 0.
    b = 1                                           # Set b to 1.
    fibonacciSequence = [0]                         # Create a list fibonacciSequence with 0 as the first element.
    for i in range(1,number):                       # For i in range from 1 to number.
        fibonacciSequence.append(b)                 # Append b to fibonacciSequence.
        a,b = b,a+b                                 # Set a to b and b to a+b.
    logging.debug("%d: %s", number, fibonacciSequence)  # Log the number and fibonacciSequence.
    return fibonacciSequence                        # Return fibonacciSequence.
    
if __name__ == "__main__":                          # If the program is run directly.
    return7 = [0,1,1,2,3,5,8]                       # Create a list return7 with the first 7 numbers of the fibonacci sequence.
    return11 = [0,1,1,2,3,5,8,13,21,34,55]          # Create a list return11 with the first 11 numbers of the fibonacci sequence.
    assert fibonacci(7) == return7, 'incorrect return for 7'    # Assert that fibonacci(7) is equal to return7.
    assert fibonacci(11) == return11, 'incorrect return for 11' # Assert that fibonacci(11) is equal to return11.
    assert fibonacci(0) == [], 'incorrect return value for 0'   # Assert that fibonacci(0) is an empty list.
    assert fibonacci(1) == [0], 'incorrect return value for 1'  # Assert that fibonacci(1) is a list with 0 as the only element.
    try:                                            # Try to run the following code.
        fibonacci(-1)                               # Call fibonacci with -1 as an argument.
    except ValueError:                              # If a ValueError is raised.
        pass                                        # Do nothing.
    else:                                           # If no ValueError is raised.
        assert False, 'fibonacci missing ValueError'# Assert False.
          
    print("All good!")                              # Print "All good!".