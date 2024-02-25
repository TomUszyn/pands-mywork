# lab5.1.2-summerMonths.py
# Program creates a tuple that stores the months of the year, from that tuple create 
# another tuple with just the summer months (May, June, July), print out the summer months one at a time.

months =("January",         # Create tumple.
         "February",
         "March",
         "April",
         "May",
         "June",
         "July",
         "August",
         "September",
         "October",
         "November",
         "December"
         )
summer = months[4:7]        # Select summer months.
for month in summer:        # Prints out result.
    print(month)