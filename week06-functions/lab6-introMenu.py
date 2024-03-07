# lab6-introMenu.py
# Schematic to build an advanced menu system
# author: Tomasz Uszynski

def displayMenu():                                          # function displayMenu
    print("What would you like to do?:")                    # print statement  
    print("\t(a) Add new student:")                         # print statement
    print("\t(v) View students:")                           # print statement
    print("\t(q) Quit:")                                    # print statement
    choice = input("Type one letter (a/v/q):").strip()      # input statement
    
    return choice                                           # return choice
#test the function
#choice = displayMenu()
#print(f"you chose {choice }")

def doAdd():                                                # function doAdd
    # we fill this in later
    print("in adding")                                      # print statement
    
def doView():                                               # function doView
    # we fill this in later
    print("in viewing")                                     # print statement
    
# main program
choice = displayMenu()                                      # assign result of function to variable choice
while(choice != 'q'):                                       # while loop
    # we could do this with lambda functions
    # we are keeping this basic for the moment
    if choice == 'a':                                       # if statement
        doAdd()                                             # function doAdd called
    elif choice == 'v':                                     # elif statement
        doView()                                            # function doView called
    else: #choice !='q':                                    # else statement
        print("\n\nplease select either a,v or q")          # print statement
    choice=displayMenu()                                    # assign result of function to variable choice