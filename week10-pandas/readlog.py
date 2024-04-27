# readlog.py
# Read in a log file, however, its format may be inconsistent and not well-structured.
# Based on code created by Andrew Beatty
# Author: Tomasz Uszynski

import pandas as pd
import re
import matplotlib.pyplot as plt

path = './data/'
logFilename = path + 'access.log.demo'
df = pd.read_csv(logFilename, sep=' ', header= None)


#print(df)
#print(df.iloc[0])

colNames = ('ip', 'dash1', 'userId', 'time', 'url', 'status code', 'size of response', 'referer', 'user agent', 'dunno')
df = pd.read_csv(logFilename, sep=' ', header= None, names=colNames)
df.drop(columns=['dash1', 'userId'], inplace=True)
#print(df)
# remove th [ from th time
# there is a lot in this line
# apply with apply the function to each element in the column and return a series
# lambda is an anonymous function
#df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())

# for the task you may want to use a normal function instead of lambda

def getNewValue(x):
    newvalue = re.search('[\w:/]+', x).group()
    # do your stuff
    return newvalue
      
df['time'] = df['time'].apply(getNewValue)
#print(df.head(3))

# Let's check the data types of the columns
#print(df.dtypes)

# this is not a normal date time format so we need to specify it
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html?highlight=to_datetime

df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')

#print(df.head(3))

#### Doing a bit of analysis
# Gettting the events that happened between 2021/02/15 23:00 and 2021/02/15 23:59:59
#df['time'] = pd.to_datetime(df['time'])
#df.set_index('time', inplace=True)

start_date = pd.to_datetime('2024/02/15 23:00')
end_date = pd.to_datetime('2024/02/15 23:59:59')

# Way one use the loc function
#newdf = df.loc[(df['time'] > start_date) & (df['time'] < end_date)]

# Way two use the series function between
#newdf = df[df['time'].between(start_date, end_date)]

# Way three set the index to the date column
# This give a whole pile of handy features
newdf = df.set_index('time')

# If we need time everyday just do:
# newdf = df.between_time('23:00', '23:59:59')
#print(newdf)

# Getting mean amount of data downloaded every 30 minutes
# sample the download sizes say every 30 minutes. It is important to note 
# that the time column is the index in this case newdf index is the time column.
downloadSamples = newdf['size of response'].resample(rule='30min').mean()
print(downloadSamples)

# Plotting the data
plt.subplots(figsize=(10, 6))
plt.plot(downloadSamples)
plt.title('Mean download size every 30 minutes', fontsize=16, weight='bold')
plt.ylabel('Mean download size', fontsize=12, weight='bold')
plt.xlabel('Datetime', fontsize=12, weight='bold')
plt.xlim(downloadSamples.index[0], downloadSamples.index[-1])
plt.ylim(downloadSamples.min() -200, downloadSamples.max() + 200)

# Customize x-axis ticks (adjust as needed)
plt.xticks(fontsize=8)


plt.show()