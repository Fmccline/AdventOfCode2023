from day import Day

class Day1(Day):

    def __init__(self):
        Day.__init__(self, 1)
        self.digits = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }

    def get_solution_a(self, input_data):
        calibrations = input_data
        nums = []
        for calibration in calibrations:
            d1 = None
            d2 = None
            for letter in calibration:
                if letter.isdigit():
                    if d1 is None:
                        d1 = letter
                    else:
                        d2 = letter
            num = d1 + d2 if d2 is not None else d1 + d1
            nums.append(int(num))
        return sum(nums)

    def get_solution_b(self, input_data):
        calibrations = input_data
        nums = []
        # first letters of the first 9 digits
        letters = set(['o', 't', 'f', 's', 'e', 'n'])
        for calibration in calibrations:
            d1 = None
            d2 = None
            for idx in range(len(calibration)):
                letter = calibration[idx]
                if letter.isdigit():
                    if d1 is None:
                        d1 = letter
                    else:
                        d2 = letter
                elif letter in letters:
                    for end_idx in range(idx + 3, idx + 6):
                        if end_idx > len(calibration):
                            break
                        sub = calibration[idx:end_idx]
                        if sub in self.digits.keys():
                            if d1 is None:
                                d1 = self.digits[sub]
                            else:
                                d2 = self.digits[sub]
            num = d1 + d2 if d2 is not None else d1 + d1
            nums.append(int(num))
        return sum(nums)
        
    def get_expected_a(self):
        return 142

    def get_expected_b(self):
        return 281