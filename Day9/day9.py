from day import Day

class Day9(Day):

    def __init__(self):
        Day.__init__(self, 9)

    def calculate_differences(self, history):
        differences = []
        for idx in range(len(history) - 1):
            differences.append(history[idx + 1] - history[idx])
        return differences

    def is_done(self, diffs):
        for diff in diffs:
            if diff != 0:
                return False
        return True

    def get_solution_a(self, input_data):
        total_num = 0
        for line in input_data:
            differences = [int(num) for num in line.split(' ')]
            next_num = 0
            while not self.is_done(differences):
                next_num += differences[-1]
                differences = self.calculate_differences(differences)
            total_num += next_num
        return total_num

    def get_solution_b(self, input_data):
        total_num = 0
        for line in input_data:
            differences = [int(num) for num in line.split(' ')]
            total_diffs = [differences]
            while not self.is_done(differences):
                differences = self.calculate_differences(differences)
                total_diffs.append(differences)
            next_num = 0
            for diff in reversed(total_diffs):
                next_num = diff[0] - next_num
            total_num += next_num
        return total_num
        
    def get_expected_a(self):
        return 114

    def get_expected_b(self):
        return 2