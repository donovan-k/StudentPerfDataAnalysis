# File for holding statistic calculations


class StatCalc:

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
