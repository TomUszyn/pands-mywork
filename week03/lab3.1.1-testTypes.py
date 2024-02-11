# lab3.1.1-testTypes.py
# Create 5 variables such as: int, float, boolean, str, list
# author: Tomasz Uszynski

i = 3                                                                                   #
fl = 3.5                                                                                #
isa = True                                                                              # Declarates different variables
memo = 'how now Brown Cow'                                                              #
lots = []                                                                               #

print('variable {} is of type:{} and value:{}'.format('i', type(i), i))                 # We use string formatting.
print('variable {} is of type:{} and value:{}'.format('fl', type(fl), fl))              # First {} is replaced by name of variable such as 'i'.
print('variable {} is of type:{} and value:{}'.format('isa', type(isa), isa))           # Second {} is replaced by type(variable)such as type(i).
print('variable {} is of type:{} and value:{}'.format('memo', type(memo), memo))        # Third {} is replaced by value of variable such as i.
print('variable {} is of type:{} and value:{}'.format('lots', type(lots), lots))        #