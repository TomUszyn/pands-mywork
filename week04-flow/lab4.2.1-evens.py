# lab4.2.1-evens.py
# Program uses a while loop to print all the even numbers from 2 to 100.
# author: Tomasz Uszynski

numberTo = 100
evenNumber = 2


while evenNumber <= numberTo:       # While loop repeatedly execute indented block of code 
                                    # as long as the condition evenNumber <= numberTo remains true.
    print(evenNumber)               # Current value of evenNum is printed using the print(evenNumber).
    evenNumber = evenNumber + 2     # evenNumber is incremented by 2.
                                    # The loop continues until exceeds the value of numberTo.