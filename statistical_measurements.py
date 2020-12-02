# File that contains Subject class which finds statistics
# File also shows mean, variance, and standard deviation of all scores
# libraries
import numpy as np
import pandas as pd
import math
import StatCalculation as sC

# read in data
df = pd.read_csv('StudentsPerformance.csv')

# access subject attributes
math_stats = sC.StatCalc(df['math score'])
read_stats = sC.StatCalc(df['reading score'])
writ_stats = sC.StatCalc(df['writing score'])


def sd_of(var):
    return math.sqrt(var)


mean_ar = np.array([math_stats.mean_of(), read_stats.mean_of(), writ_stats.mean_of()])
var_ar = np.array([math_stats.var_of(), read_stats.var_of(), writ_stats.var_of()])
sd_ar = np.array([sd_of(math_stats.var_of()), sd_of(read_stats.var_of()), sd_of(writ_stats.var_of())])

data = {'mean': mean_ar, 'variance': var_ar, 'standard deviation': sd_ar}
new_df = pd.DataFrame(data=data, index=['math', 'reading', 'writing'])
print(new_df)
