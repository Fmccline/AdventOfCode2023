from util import read_file_to_list
from day import Day


class Day2(Day):

    def __init__(self):
        Day.__init__(self, 2)

    def get_expected_a(self):
        return 8

    def get_solution_a(self, test=True):
        input_data = self.get_input() if not test else self.get_test_input_a()
        return None
