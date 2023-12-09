import sys 


def read_file_to_list(filename):
    contents = []
    with open(filename) as file:
        for line in file:
            contents.append(line)
    return contents


def get_calibations(calibrations):
    digits = {
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
                    if sub in digits.keys():
                        if d1 is None:
                            d1 = digits[sub]
                        else:
                            d2 = digits[sub]
        num = d1 + d2 if d2 is not None else d1 + d1
        nums.append(int(num))
    return sum(nums)


def get_calibations_test(calibrations):
    num = get_calibations(calibrations)
    correct = 281
    test = 'PASSED\n' if num == correct else 'FAILED\n'
    test += f'Expected {correct} and got {num}'
    return test


if __name__ == '__main__':
    is_test = True
    if (len(sys.argv) > 1):
        is_test = False
    
    filename = 'test_b.txt' if is_test else 'input.txt'
    calibrations = read_file_to_list(filename)
    if is_test:
        print(get_calibations_test(calibrations))
    else:
        print(get_calibations(calibrations))

