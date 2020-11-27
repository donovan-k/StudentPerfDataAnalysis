# libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# read in data
df = pd.read_csv('StudentsPerformance.csv', index_col=0)

# set width of bar
barWidth = 0.25

# set height of bar
group_male = df.drop('female')
group_female = df.drop('male')

male_well_math = group_male.where(group_male['math score'] > 80)
fem_well_math = group_female.where(group_female['math score'] > 80)

male_well_read = group_male.where(group_male['reading score'] > 80)
fem_well_read = group_female.where(group_female['reading score'] > 80)

male_well_writ = group_male.where(group_male['writing score'] > 80)
fem_well_writ = group_female.where(group_female['writing score'] > 80)


def well_counter(group, score):
    group_count = 0
    for j in group[score]:
        if j > 80:
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
