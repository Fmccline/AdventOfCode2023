from util import read_file_to_list


class Day:

    def __init__(self, num):
        self.num = num

    def get_solution_a(self, input_data):
        pass

    def get_solution_b(self, input_data):
        pass
        
    def get_expected_a(self):
        pass

    def get_expected_b(self):
        pass

    def get_solutions(self):
        input_data = self.get_full_input()
        a = self.get_solution_a(input_data)
        b = self.get_solution_b(input_data)
        return a, b

    def get_full_input(self):
        return read_file_to_list(f'Day{self.num}/input.txt')

    def get_test_input_a(self):
        return read_file_to_list(f'Day{self.num}/test_a.txt')
    
    def get_test_input_b(self):
        return read_file_to_list(f'Day{self.num}/test_b.txt')

    def test_solution(self, expected, result):
        print(f"{'FAILED' if expected != result else 'PASSED'}")
        print(f'Expected {expected} and got {result}')

    def test_solution_a(self):
        input_data = self.get_test_input_a()
        expected = self.get_expected_a()
        result = self.get_solution_a(input_data)
        self.test_solution(expected, result)

    def test_solution_b(self):
        input_data = self.get_test_input_b()
        expected = self.get_expected_b()
        result = self.get_solution_b(input_data)
        self.test_solution(expected, result)
