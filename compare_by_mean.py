# File compares male and female scores by mean and plots them on a bar graph
# libraries
import statistical_measurements as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class GenderMean:  # class is used to create objects for groups and differentiate their subjects

    def __init__(self, math_sb, read_sb, writ_sb):
        self.math_sb = math_sb
        self.read_sb = read_sb
        self.writ_sb = writ_sb


com_df = pd.read_csv('StudentsPerformance.csv', index_col=0)
male = com_df.drop('female')
fem = com_df.drop('male')

male_data = GenderMean(male['math score'], male['reading score'], male['writing score'])
fem_data = GenderMean(fem['math score'], fem['reading score'], fem['writing score'])

male_math_stats = sm.Subject(male_data.math_sb)
fem_math_stats = sm.Subject(fem_data.math_sb)

male_read_stats = sm.Subject(male_data.read_sb)
fem_read_stats = sm.Subject(fem_data.read_sb)

male_writ_stats = sm.Subject(male_data.writ_sb)
fem_writ_stats = sm.Subject(fem_data.writ_sb)

bars1 = [male_math_stats.mean_of(), fem_math_stats.mean_of()]   # Average math score
bars2 = [male_read_stats.mean_of(), fem_read_stats.mean_of()]  # Average reading score
bars3 = [male_writ_stats.mean_of(), fem_writ_stats.mean_of()]  # Average writing score

# set width of bar
barWidth = 0.25

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
