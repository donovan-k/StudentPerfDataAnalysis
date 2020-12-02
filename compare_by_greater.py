# File compares male and female scores by the amount that are greater than 80
# libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ScoreGreater as sG

# read in data
df = pd.read_csv('StudentsPerformance.csv', index_col=0)

# set width of bar
barWidth = 0.25

# set height of bar
group_male = sG.ScoreGreater(df.drop('female'), 80)
group_female = sG.ScoreGreater(df.drop('male'), 80)

male_well_math = group_male.math_well()
fem_well_math = group_female.math_well()

male_well_read = group_male.read_well()
fem_well_read = group_female.read_well()

male_well_writ = group_male.writ_well()
fem_well_writ = group_female.writ_well()


def well_counter(group, score):
    group_count = 0
    for j in group[score]:
        if j > group_male.gr_good:
            group_count = group_count + 1
    return group_count


male_math_count = well_counter(male_well_math, 'math score')
fem_math_count = well_counter(fem_well_math, 'math score')
male_read_count = well_counter(male_well_math, 'reading score')
fem_read_count = well_counter(fem_well_math, 'reading score')
male_writ_count = well_counter(male_well_math, 'writing score')
fem_writ_count = well_counter(fem_well_math, 'writing score')


bars1 = [male_math_count, fem_math_count]   # Did well in math
bars2 = [male_read_count, fem_read_count]  # Did well in reading
bars3 = [male_writ_count, fem_writ_count]  # Did well in writing

# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='Math')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='Reading')
plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='Writing')

# Add xticks on the middle of the group bars
plt.xlabel('Gender(male or female)', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['male', 'female'])

# Create legend & Show graphic
plt.legend()
plt.show()
