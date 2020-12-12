# Class file for making student objects
import numpy as np
import StatCalculation as sc


class StudentData:
    def __init__(self, data):
        self.data = data
        self.gender = data['gender']
        self.race = data['race/ethnicity']
        self.parent_edu = data['parental level of education']
        self.lunch = data['lunch']
        self.test_pre = data['test preparation course']

    def gr_mean(self, select):
        mean_each = np.zeros((5, 3))
        subject = np.array(['math score', 'reading score', 'writing score'])
        gender_df = self.data[self.gender == select[0]]
        race_df = self.data[self.race == select[1]]
        parent_df = self.data[self.parent_edu == select[2]]
        lunch_df = self.data[self.lunch == select[3]]
        pretest_df = self.data[self.test_pre == select[4]]

        for i in range(3):
            mean_each[0, i] = sc.StatCalc(gender_df[subject[i]]).mean_of
            mean_each[1, i] = sc.StatCalc(race_df[subject[i]]).mean_of
            mean_each[2, i] = sc.StatCalc(parent_df[subject[i]]).mean_of
            mean_each[3, i] = sc.StatCalc(lunch_df[subject[i]]).mean_of
            mean_each[4, i] = sc.StatCalc(pretest_df[subject[i]]).mean_of

        return mean_each

