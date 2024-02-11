# lab3.1.7- answers.py
# Solve problem with printing message.
# author: Tomasz Uszynski

# 6. Why does this expression cause an error? How can you fix it? 
#message = 'I have eaten ' + 99 + ' burritos.'
#print (message)

# It is because we can't concatenate in Python two different tyoe such as string an integer.
# The easiest way is convert integer to string.

message = 'I have eaten ' + str(99) + ' burritos.'
print (message)

#We can also use f.string to avoid errors. Prefix f indicate exceptions enclosed in curly braces.
#{burritos_count} is a placeholder for a variable called burritos_count. burritos_count is integer.

buritos_count = 99
message = f'I have eaten {buritos_count} burritos.'
print(message)

# 7. Why is eggs a valid variable name while 100 is invalid?

# eggs is valid variable because this is sting and 100 is invalid because this is integer.


# 8. What three functions can be used to get the integer, floating-point number, 
# or string version of a value?

# There are int(), float() and str().