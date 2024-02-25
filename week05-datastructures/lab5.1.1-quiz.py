# lab5.1.1-quiz.py
# Program prints out types of varaible listed below.
# author: Tomasz Uszynski

# What are the variable types of the following variables in the code above
# a. numberOfQuestions
# b. averageAge
# c. debugMode
# d. name
# e. ages
# f. months
# g. months[1]
# h. book
# i. stuff
# j. stuff[2]
# k. someone
# l. someone["firstname"]
# m. me
# n. me["teaching"]
# o. me["teaching"][0]["semester"]
# p. me["teaching"][0]["coursename"]

# We have a list of different variable. We are checking type of each variable and print out results.
numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "joe"
ages = []
months = ('Jan', 'Feb', 'Mar')
book = {}
stuff = [ 12 , 'Fred', False, {}]
someone = dict(firstname = "joe")
print(someone)
me = {
"firstName" : "Andrew",
"teaching" : [{
        "courseName" : "programming",
        "semester" : 1
        },{
        "courseName" : "Data Representation",
        "semester" : 2
}
]
}

print("a. numberOfquestion type is", type(numberOfQuestions))  # Prints out type of value.
print("b. averageAge type is", type(averageAge))               # Prints out type of value.
print("c. debugMode type is", type(debugMode))                 # Prints out type of value.
print("d. name type is", type(name))                           # Prints out type of value.
print("e. ages type is", type(averageAge))                     # Prints out type of value.
print("f. months type is", type(months))                       # Prints out type of value.
print("g. months[1] type is", type(months[1]))                 # Prints out type of first element.
print("h. book type is", type(book))                           # Prints out type of value.
print("i. stuff type is", type(stuff))                         # Prints out type of value.
print("j. stuff[2] type is", type(stuff[2]))                   # Prints out type of value.
print("k. someone type is", type(someone))                     # Prints out type of value. 
print('l. someone["firstname"] is',type(someone["firstname"])) # Prints out type of value.
print('m. me type is', type(me))                               # Prints out type of value.        
print('n. me["teaching"] type is', type(me["teaching"]))       # Prints the type of the value associated 
                                                               # with the key "teaching" in the dictionary 'me'.
    
print('o. me["teaching"][0]["semester"] type is', 
      type(me["teaching"][0]["semester"]))                     # Prints type of value associated with key "semester"
                                                               # in first element of list 'me["teaching"]'.
print('p. me["teaching"][0]["coursename] type is',
       type(me["teaching"][0].get("coursename")))              # Prints type of value associated with key "coursename"
                                                               # in first element of list 'me["teaching"]'. Get() method 
                                                               # retrieves the value associated with a specified key 
                                                               # from a dictionary. If the key is not found it returns None.