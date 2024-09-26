# import pandas
import pandas as pd
# read in the data
schools = pd.read_csv('schools.csv')
# preview the data
schools.head()
# STEP 1 - Find schools wth best math scores
# define the threshold for 80% of the max score
threshold = 0.8 * 800
# subset data to get schools with math scores >= 80% of max score
best_math_schools = schools[schools['average_math'] >= threshold][['school_name','average_math']]
# sort schools by average_math scores in descending order
best_math_schools = best_math_schools.sort_value(by='average_math', ascending = False)
# STEP 2 - Identify top 10 performeing schools
# create new column by summing math, reading, and writing scores
schools['total_SAT']= schools['average_math'] + schools['average_reading'] + schools['average_writing']
# sort df by "total_SAT" in descending order and select top 10 schools
top_10_schools = schools[['school_name', 'total_SAT']].sort_values(by= 'total_SAT',ascending= False).head(10)
# STEP 3 - Locating NYC borough with largest SD in SAT performance
# group data by borough and calculate no of schools, mean, and SD of total_SAT, also round to 2 decimal place
borough_stats= schools.groupby('borough').agg(num_schools= ('school_name', 'count'), average_SAT = ('total_SAT', 'mean'), std_SAT= ('total_SAT','std')).round(2)
# find borough with largest SD of total_SRT
largest_std_dev = borough_stats[borough_stats['std_SAT'] == borough_stats['std_SAT'].max()]
# reset index to include borough name in the DF
largest_std_dev = largest_std_dev.reset_index()
# display result
print(largest_std_dev)
