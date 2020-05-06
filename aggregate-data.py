from datetime import datetime as dt
import pandas as pd 
import csv

# Load the CSVs
df = pd.read_csv('data/january-through-april-cats.csv')

aggregate_values = {}

for i, row in df.iterrows():
	time_value = dt.strptime(row['date'], '%Y-%m-%d %H:%M:%S').date()
	if time_value in aggregate_values.keys():
		aggregate_values[time_value] += row['cats']
	else:
		aggregate_values[time_value] = row['cats']

with open('data/aggregate-daily-values-cats.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(['date', 'interest'])
    for key, value in aggregate_values.items():
    	w.writerow([str(key), str(value)])

