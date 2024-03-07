# lab6.3-scope.py
# More messing with functions. Variable scope.
# author: Tomasz Uszynski

# What is the scope of a variable? The scope of a variable is the part of the program 
# where the variable can be accessed.
# This program is to demonstrate the scope of variable. To understand the scope of variables, 
# we need to understand the following: 
# 1. Local variables: variables declared inside a function.
# 2. Global variables: variables declared outside a function.
# 3. The scope of a variable is the part of the program where the variable can be accessed.
# 4. The lifetime of a variable is the period of time during which the variable exists in memory.
# 5. The lifetime of a variable is the same as its scope.
# 6. The scope of a variable is determined by where the variable is declared.
# 9. A local variable can have the same name as a global variable.
# 10. A local variable will take precedence over a global variable.
# 11. A global variable can be accessed from inside a function.
# 12. A local variable cannot be accessed from outside a function.
# 13. A local variable can be accessed from inside a function.

# We want you to use global variables. They are a bad practice.

x = 999                     # x is a global variable.

def fun(num):               # Try do not have varialble outside function
    print(num)
    
def fun2(x2):                   # x2 is a local variable
    print(f"in fun2 x {x2} ")   # print the value of x2.
    #global x                   # x is a global variable.
    x = 21                      # x is a local variable.                        
    print(f"in fun2 x {x2} ")   # print the value of x2


fun2(x)                         # call fun2 with x as an argument where x is a global variable.
print(f"after fun2 x is {x} ")  # print the value of x.