import sys
from Day1.day1 import Day1
from Day2.day2 import Day2
from Day3.day3 import Day3
from Day4.day4 import Day4
from Day5.day5 import Day5
from Day6.day6 import Day6


days = {
    1: Day1(),
    2: Day2(),
    3: Day3(),
    4: Day4(),
    5: Day5(),
    6: Day6(),
}


def get_solutions(day):
    is_test = len(sys.argv) <= 2
    if is_test:
        day.test_solution_a()
        day.test_solution_b()
    else:
        a, b = day.get_solutions()
        print(f'{a}\n{b}')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        day_num = int(sys.argv[1])
        day = days[day_num]
        get_solutions(day)
    else:
        for day in days.values():
            get_solutions(day)
            print()
    