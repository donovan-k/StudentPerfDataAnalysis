import statistical_measurements
import pandas as pd
import unittest


class TestStatMeasurements(unittest.TestCase):

    def test_sum(self):
        df = pd.read_csv('test_file.csv')
        sub = statistical_measurements.Subject(df['numbers'])
        self.assertEqual(sub.sum_of(), 15)

    def test_mean(self):
        df = pd.read_csv('test_file.csv')
        sub = statistical_measurements.Subject(df['numbers'])
        self.assertEqual(sub.mean_of(), 3)

    def test_var(self):
        df = pd.read_csv('test_file.csv')
        sub = statistical_measurements.Subject(df['numbers'])
        self.assertEqual(sub.var_of(), 2.5)

