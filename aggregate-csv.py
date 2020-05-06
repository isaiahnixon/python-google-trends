from datetime import datetime as dt
import pandas as pd 
import csv

# Load the CSVs
df1 = pd.read_csv('data/january-through-september.csv')
df2 = pd.read_csv('data/october-through-november.csv')
df3 = pd.read_csv('data/december-through-april.csv')
df = df1.append(df2, ignore_index=True).append(df3, ignore_index=True)

aggregate_values = {}

for i, row in df.iterrows():
	time_value = dt.strptime(row['date'], '%Y-%m-%d %H:%M:%S').date()
	if time_value in aggregate_values.keys():
		aggregate_values[time_value] += row['toilet paper']
	else:
		aggregate_values[time_value] = row['toilet paper']

with open('data/aggregate-daily-values.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.writer(f)
    w.writerow(['date', 'interest'])
    for key, value in aggregate_values.items():
    	w.writerow([str(key), str(value)])

