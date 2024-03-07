# lab6.1.2-flexibleArguments.py
# More messing with functions. Flexible arguments.
# author: Tomasz Uszynski

print(1, 2, 3, end="\t", sep ="")           # sep and end can be swapped with position and result will be the same.
print("Hi")

# unnamed args
def fun1(*args):            # *args is a tuple of arguments. It can be empty. * is a splat operator. 
                            # We use it to indicate that we can pass any number of arguments.
    print(type(args))       # <class 'tuple'>
    for val in args:        # args is a tuple, so we can iterate over it.
        print(val)          # print each value in the tuple.

#fun1("a", "b", "c")        # call fun1 with 3 arguments.

# keyword arguments
def fun2(**kwargs):          # **kwargs is a dictionary of keyword arguments. It can be empty.
                             # ** is a splat operator. We use it to indicate that we can pass 
                             # any number of keyword arguments.
    print(type(kwargs))      # <class 'dict'>
    print(kwargs)            # print the dictionary of keyword arguments.
#   for val in kwargs:       # iterate over the dictionary of keyword arguments.
#       print(val)           # print each key in the dictionary of keyword arguments.

#fun2(name="joe", age=21, gender="M")    # call fun2 with 3 keyword arguments.

# sample code
def ave(*values):                       # *values is a tuple of arguments. It can be empty.
    number_of_values = len(values)      # get the number of values in the tuple.
    sum = 0                             # initialise sum to 0.
    for value in values:                # iterate over the values in the tuple.
        sum += value                    # add the value to the sum.
    
    average = sum / number_of_values    # calculate the average.
    return average, sum                 # return the average and the sum.

av1, sum_of_numbers =ave(1,2,3,4,5,6)   # call ave with 6 arguments.
print(f"Average is {av1} and sum is {sum_of_numbers}.") # print the average and the sum.