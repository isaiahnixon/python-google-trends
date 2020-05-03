import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime as dt
import pandas as pd 
import numpy as np

# Load the csv
df1 = pd.read_csv('data/october-through-november.csv')
df2 = pd.read_csv('data/december-through-april.csv')
df = df1.append(df2, ignore_index=True)

time_values = []
interest_values = []

for i, row in df.iterrows():
	time_values.append(mdates.date2num(dt.strptime(row['date'], '%Y-%m-%d %H:%M:%S')))
	interest_values.append(row['toilet paper'])

fig, ax = plt.subplots()

ax.set_title('Interest in Toilet Paper (Google Trends)')
ax.set_ylabel('Interest')
ax.plot_date(time_values, interest_values, linestyle='-', marker='.', color='black')

# For data within the same day.
#hfmt = mdates.DateFormatter('%H:%M:%S')
#ax.set_xlabel('Time')

# For larger data sets.
hfmt = mdates.DateFormatter('%b %d %Y')
ax.set_xlabel('Date')

ax.xaxis.set_major_formatter(hfmt)
plt.gcf().autofmt_xdate()

plt.show()
