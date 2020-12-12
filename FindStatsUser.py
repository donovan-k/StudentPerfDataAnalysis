# This file will ask for users inputs for groups such as male or female, race(A,B,...),
#   parental level of education, lunch, and test preparation course and then display the groups
#   you have chosen and their average score in math, reading, and writing
import numpy as np
import pandas as pd
import json
import StudentData as sD
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')
with open('possibleGroups.json') as f:
    pos_ans = json.loads(f.read())

df_array = np.array(df)
cate = np.array(['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course'])
students = list(range(5))


def answer_questions(stud):
    for i in range(len(cate)):
        while not stud[i] in pos_ans[cate[i]]:
            print(cate[i], ', Possible choices include: ', pos_ans[cate[i]])
            stud[i] = input('--> ')
    return stud


students = np.array(answer_questions(students))

sDf = sD.StudentData(df)
st_mean = sDf.gr_mean(students)

bars1 = st_mean[:, 0]  # Average math score
bars2 = st_mean[:, 1]  # Average reading score
bars3 = st_mean[:, 2]  # Average writing score

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
plt.xlabel('Score based on groups entered by user', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], students)

# Create legend & Show graphic
plt.legend()
plt.show()
