from pytrends.request import TrendReq

# This file is optimized so that the Google Trends API will not be overloaded.
# It can take a long time to run.

# CONFIG
kw_list=['toilet paper']

# Start datetime
year_start = 2019
month_start = 1
day_start = 1
hour_start = 0

# End datetime
year_end = 2019
month_end = 9
day_end = 30
hour_end = 23

# Sleep between calls
# Note: There should be one call per week of data requested.
sleep = 120

# CSV name
csv_name = 'january-through-september'

# Establish connection
pytrend = TrendReq(hl='en-US', tz=360, timeout=(10,25), retries=3, backoff_factor=1)

# Get the data and save it to a csv.
pytrend.get_historical_interest(kw_list, year_start=year_start, month_start=month_start, day_start=day_start, hour_start=hour_start, year_end=year_end, month_end=month_end, day_end=day_end, hour_end=hour_end, cat=0, geo='', gprop='', sleep=sleep).to_csv('data/' + csv_name + '.csv')