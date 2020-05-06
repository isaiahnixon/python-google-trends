import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime as dt
import pandas as pd 
import numpy as np

# Load the csv
df1 = pd.read_csv('data/aggregate-daily-values.csv')
df2 = pd.read_csv('data/aggregate-daily-values-covid-19.csv')
df3 = pd.read_csv('data/aggregate-daily-values-cats.csv')

time_values1 = []
interest_values1 = []

time_values2 = []
interest_values2 = []

time_values3 = []
interest_values3 = []

for i, row in df1.iterrows():
	time_values1.append(mdates.date2num(dt.strptime(row['date'], '%Y-%m-%d'))) #dates
	# time_values.append(mdates.date2num(dt.strptime(row['date'], '%Y-%m-%d %H:%M:%S'))) #datetime
	interest_values1.append(row['interest'])

for i, row in df2.iterrows():
	time_values2.append(mdates.date2num(dt.strptime(row['date'], '%Y-%m-%d'))) #dates
	# time_values.append(mdates.date2num(dt.strptime(row['date'], '%Y-%m-%d %H:%M:%S'))) #datetime
	interest_values2.append(row['interest'])

for i, row in df3.iterrows():
	time_values3.append(mdates.date2num(dt.strptime(row['date'], '%Y-%m-%d'))) #dates
	# time_values.append(mdates.date2num(dt.strptime(row['date'], '%Y-%m-%d %H:%M:%S'))) #datetime
	interest_values3.append(row['interest'])

fig, ax = plt.subplots()

ax.set_title('Interest in COVID-19 (Google Trends)')
ax.set_ylabel('Interest')
ax.plot_date(time_values1, interest_values1, linestyle='-', marker='o', color='blue', label='Toilet Paper')
ax.plot_date(time_values2, interest_values2, linestyle='-', marker='o', color='black', label='COVID-19')
ax.plot_date(time_values3, interest_values3, linestyle='-', marker='o', color='red', label='Cats')


# For data within the same day.
#hfmt = mdates.DateFormatter('%H:%M:%S')
#ax.set_xlabel('Time')

# For larger data sets.
hfmt = mdates.DateFormatter('%b %d %Y')
ax.set_xlabel('Date')

ax.xaxis.set_major_formatter(hfmt)
plt.gcf().autofmt_xdate()
plt.legend()
plt.show()
