# createdf.py
# Create data frame from list of lists
# Author: Tomasz Uszynski

import pandas as pd

listDAta= [
    ['John', 'math', 23],
    ['John', 'programming', 66],
    ['Mary', 'math', 45],
    ['Mary', 'programming', 33],
    ['Mark', 'SIEM', 57],
    ['Mark', 'programming', 70],
    ['Mark', 'math', 73],
    ['John', 'programming', 61]
]

df = pd.DataFrame(listDAta, columns=['name', 'course', 'grade'])
print(df.head(3))
print(df.describe())
print(type(df.describe()))

# Writting to files.
path = "./data/"
cvsFile = path + 'grades.csv'
df.to_csv(cvsFile)

excelFile = path + 'grades.xlsx'
df.to_excel(excelFile, sheet_name='data', index=False)
with pd.ExcelWriter(excelFile, engine='openpyxl', mode='a') as writer:
    # index is true becuase that contains the information about what the numbers are
    df.describe().to_excel(writer, sheet_name='summary')
    
mean = df.describe().loc['mean', 'grade']
print(mean)
#or
mean = df['grade'].mean()
print(mean)