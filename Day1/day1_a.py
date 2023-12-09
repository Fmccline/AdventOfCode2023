import sys 


def read_file_to_list(filename):
    contents = []
    with open(filename) as file:
        for line in file:
            contents.append(line)
    return contents


def get_calibations(calibrations):
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


def get_calibations_test(calibrations):
    num = get_calibations(calibrations)
    correct = 142
    test = 'PASSED\n' if num == correct else 'FAILED\n'
    test += f'Expected {correct} and got {num}'
    return test


if __name__ == '__main__':
    is_test = True
    if (len(sys.argv) > 1):
        is_test = False
    
    filename = 'test_a.txt' if is_test else 'input_a.txt'
    calibrations = read_file_to_list(filename)
    if is_test:
        print(get_calibations_test(calibrations))
    else:
        print(get_calibations(calibrations))

