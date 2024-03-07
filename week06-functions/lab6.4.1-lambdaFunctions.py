# lab6.4.1-lambdaFunctions.py
# More messing with functions. Anonymous functions.
# author: Tomasz Uszynski
'''
x = lambda arg1: arg1 ** 2                                  # lambda function to square a number.

answer  = x(4)                                              # call the lambda function with 4 as an argument.
print(answer)                                               # print the answer.
'''
#businesstype = "standard"                                  # standard VAT rate
businesstype = "reduced"                                    # reduced VAT rate

vatcalc = lambda amount: amount * 0.23                      # standard VAT rate

if businesstype == "reduced":                               # if the business type is reduced.
    vatcalc = lambda amount: amount * 0.135                 # reduced VAT rate
    
cash = 10                                                   # amount of cash

print(vatcalc(cash))                                        # print the VAT on the cash.                                        

# sort a list
numbers = [2, 33, 55, 1, 4]                                 # list of numbers.
sortednumbers = sorted(numbers)                             # sort the numbers.

print(f"{numbers} sorted is {sortednumbers}")               # print the sorted numbers.

# sort dictionary
data = [{'first': 'Guido', 'last':'Van Rossum', 'YOB':1956},#
      {'first': 'Grace', 'last':'Hopper', 'YOB':1906},      # list of dictionaries.
      {'first': 'Alan', 'last':'Turing', 'YOB':1912}]       #

sorteddata = sorted(data, key=lambda x:x["first"])          # sort the data by the first name.
#print(f"{data} sorted is {sorteddata}")                    # print the sorted data.

for item in sorteddata:                                     # for each item in the sorted data.
    print(item)                                             # print each item in the sorted data.
