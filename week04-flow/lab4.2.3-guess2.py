# 4.2.2-guess2.py
# Program prompts the user to guess a number, the program should keep prompting the user 
# to guess the number until the user gets the right one.
# author: Tomasz Uszynski

guessTheNumber = 30                                        # Declarates target number.

guess = int(input("Please guess the number: "))            # User enters their guess.

while guess != guessTheNumber:                             # loop  continues executing as long as the user’s guess 
    if guess < guessTheNumber:                             # (guess) is not equal to the target number (guessTheNumber)
        print("Too low.")                                  # Gives sugestion.
    else:                                                  
        print("Too high.")                                 # Gives sugestion.
    guess =int(input("Please guess again: "))              

print("Well done! yes the number was:", guessTheNumber)    # Prints result.