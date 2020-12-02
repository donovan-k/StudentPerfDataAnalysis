# File that contains Subject class which finds statistics
# File also shows mean, variance, and standard deviation of all scores
# libraries
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
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

bars1 = mean_ar   # Bar for mean comparison
bars2 = var_ar  # Bar for variance comparison
bars3 = sd_ar  # bar for standard deviation comparison

# set width of bar
barWidth = 0.25

# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='Mean')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='Variance')
plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='SD')

# Add xticks on the middle of the group bars
plt.xlabel('Type of Measurement', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['math', 'reading', 'writing'])

# Create legend & Show graphic
plt.legend()
plt.savefig('compare_subjects.png')
