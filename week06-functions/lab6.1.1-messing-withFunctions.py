# lab6.1.1-messing-withFunctions.py
# Messing with functions to demonstrate the defining and using functions.
# author: Tomasz Uszynski

#x, y, z = (1, 2, 3)
#print(x, y, z, sep="", end="")
#print(f"{x}-{y} {z}")               # This way of printing by default put a new line.
#print("{} {}--{}".format(x, y, z))  # Should not be used anymore.

def topower(number, power=3):  # power by default set to 3, but if we give argument
                               # to topower such as topower(num,anynumber)
                               # it will be power by any number but without agrument 
                               # it will be default -see line 19.
    #print(number)
    return (number ** power)

#ans = topower(23)
#print(f"We got {ans}")
num = 45 # This is the number we want to raise to the power of 3.

#print(f"and {num} is {topower(num,5)}")
print(f"and {num} is {topower(num)}")   # This will use the default power of 3.