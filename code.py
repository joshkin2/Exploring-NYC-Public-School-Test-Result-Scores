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
top_10
