# lab6.2.1-readinnumbers.py
# Read in two numbers and multiply them.
# author: Tomasz Uszynski

def readNum(message = "Enter a number: "):                  # message is a default argument.    
    num = False                                             # num is a boolean variable.
    while (not num):                                        # while not num is True.
        try:                                                # try to do this.
            num = int(input(message))                       # read in a number.
        except ValueError:                                  # if there is a ValueError.
            print ("That was not a number, ", end="")       # print this message.
    return num                                              # return the number.

num1 = readNum()                                            # call readNum with no arguments.
num2 = readNum("Enter second number: ")                     # call readNum with an argument.

answer = num1 * num2                                        # multiply the two numbers.
print(f"Answer is {answer}.")                               # print the answer.