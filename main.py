import sys
from Day1.day1 import Day1
from Day2.day2 import Day2


days = {
    1: Day1(),
    2: Day2(),
}



if __name__ == '__main__':
    day_num = int(sys.argv[1])
    is_test = len(sys.argv) <= 2
    day = days[day_num]
    if is_test:
        day.test_solution_a()
        day.test_solution_b()
    else:
        a, b = day.get_solutions()
        print(f'{a}\n{b}')