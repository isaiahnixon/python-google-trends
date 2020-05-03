from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd 
import numpy as np

pytrend = TrendReq(hl='en-US', tz=360, timeout=(10,25), retries=2, backoff_factor=0.1)
kw_list=['toilet paper']

# March 17th
#historical_interest__raw_df = pytrend.get_historical_interest(kw_list, year_start=2020, month_start=3, day_start=17, hour_start=0, year_end=2020, month_end=3, day_end=17, hour_end=23, cat=0, geo='', gprop='', sleep=6)

# Month of March
historical_interest__raw_df = pytrend.get_historical_interest(kw_list, year_start=2020, month_start=3, day_start=1, hour_start=0, year_end=2020, month_end=3, day_end=31, hour_end=23, cat=0, geo='', gprop='', sleep=6)

time_values = []
interest_values = []

for i, row in historical_interest__raw_df.iterrows():
	time_values.append(mdates.date2num(i))
	interest_values.append(row['toilet paper'])

fig, ax = plt.subplots()

ax.set_title('Interest in Toilet Paper (Google Trends)')
ax.set_ylabel('Interest')
ax.plot_date(time_values, interest_values, linestyle='-', marker='.', color='black')

# For data within the same day.
#hfmt = mdates.DateFormatter('%H:%M:%S')
#ax.set_xlabel('Time')

# For data within the same month.
hfmt = mdates.DateFormatter('%b %d')
ax.set_xlabel('Date')

ax.xaxis.set_major_formatter(hfmt)
plt.gcf().autofmt_xdate()

plt.show()
