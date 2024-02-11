# Program reads in a string and strips any leading or trailing spaces.
# It also converts all the letters to lower case.
# It then outputs the lengths of the original string and the normalised one.
# author: Tomasz Uszynski


rawString = input("Please enter a string: ")                                                        # Stores value string as rawString.
normalisedString = rawString.strip().lower()                                                        # Swaps capital letters to lower cases.
lenghtOfRawString = len(rawString)                                                                  # Checks length of value.
lenghtOfNormalised = len(normalisedString)                                                          # Checks length of value.
print(f"That String normalised is: {normalisedString}")                                             # Prints out results.
print(f"We reduced the input string from {lenghtOfRawString} to {lenghtOfNormalised} characters")   # Prints out results.