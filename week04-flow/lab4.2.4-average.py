# lab4.2.4-average.py
# Program reads in numbers until user enters 0 and print out each of the numbers entered and the
# average of them.
# author: Tomasz Uszynski


numbers = []                                            # Creates empty list.

number = int(input("enter number (0 to quit): "))       # Entered number is converted to an integer 
                                                        # and stored in variable number.
                                                        
# The program enters a while loop that continues as long as the value of number is not equal to 0.
# Inside the loop:
# The current number appens to the numbers list.
# The program asks the user to enter another number (or 0 to quit).
# The new input is again converted to an integer and assigned to number.

while number != 0:
 numbers.append(number)

 number = int(input("enter another (0 to quit): "))

# After the user quits (by entering 0), the program exits the loop.
# It then iterates through the numbers list using a for loop.
# For each value in the list, it prints the value.
 
for value in numbers:
 print (value)

# The average of the entered numbers is calculated by dividing the sum of all numbers by the total count.
# The result is stored in the variable average.

average = float(sum(numbers)) / len(numbers)

# The program prints the average using an f-string.

print (f"The average is {average}")