# File holding class is used to create objects for groups and methods for scoring better than given


class ScoreGreater:

    def __init__(self, gr_name, gr_good):
        self.gr_name = gr_name
        self.gr_good = gr_good

    def math_well(self):
        return self.gr_name.where(self.gr_name['math score'] > self.gr_good)

    def read_well(self):
        return self.gr_name.where(self.gr_name['reading score'] > self.gr_good)

    def writ_well(self):
        return self.gr_name.where(self.gr_name['writing score'] > self.gr_good)
