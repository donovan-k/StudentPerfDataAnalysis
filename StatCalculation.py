# File for holding statistic calculations
import numpy as np


class StatCalc:

    def __init__(self, sb_name):
        self.sb_name = np.array(sb_name)
        self.sum_of = np.sum(self.sb_name)
        self.mean_of = self.sum_of / len(sb_name)
        # The variance was found by using a more closed form of the summation formula for sample variance
        # 1/(n-1) * (sum((xi - x_bar)^2) where the only sums need to compute are now xi and xi^2
        self.var_of = (1 / (len(self.sb_name) - 1)) * (np.sum(np.square(self.sb_name)) - 2 * self.mean_of *
                                                       self.sum_of + len(self.sb_name) * self.mean_of ** 2)
