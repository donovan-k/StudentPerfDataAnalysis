# libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


class Subject:

    def __init__(self, sb_name):
        self.sb_name = sb_name

    def sum_of(self):
        return sum(self.sb_name)

    def mean_of(self):
        return sum(self.sb_name) / len(self.sb_name)

    def var_of(self):
        tot = 0
        x_bar = sum(self.sb_name) / len(self.sb_name)
        x = self.sb_name
        for i in range(len(x)):
            val = x[i] - x_bar
            val = val ** 2
            tot = tot + val
        return tot / (len(x) - 1)


# read in data
df = pd.read_csv('StudentsPerformance.csv')

# access subject attributes
math_stats = Subject(df['math score'])
read_stats = Subject(df['reading score'])
writ_stats = Subject(df['writing score'])


def sd_of(var):
    return math.sqrt(var)


mean_ar = np.array([math_stats.mean_of(), read_stats.mean_of(), writ_stats.mean_of()])
var_ar = np.array([math_stats.var_of(), read_stats.var_of(), writ_stats.var_of()])
sd_ar = np.array([sd_of(math_stats.var_of()), sd_of(read_stats.var_of()), sd_of(writ_stats.var_of())])

data = {'mean': mean_ar, 'variance': var_ar, 'standard deviation': sd_ar}
new_df = pd.DataFrame(data=data, index=['math', 'reading', 'writing'])
print(new_df)
