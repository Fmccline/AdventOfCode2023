import sys
from Day1.day1 import Day1
from Day2.day2 import Day2
from Day3.day3 import Day3
from Day4.day4 import Day4
from Day5.day5 import Day5
from Day6.day6 import Day6
from Day7.day7 import Day7
from Day8.day8 import Day8
from Day9.day9 import Day9
from Day10.day10 import Day10
from Day11.day11 import Day11
from Day12.day12 import Day12
from Day13.day13 import Day13
from Day14.day14 import Day14
from Day15.day15 import Day15


days = {
    1: Day1(),
    2: Day2(),
    3: Day3(),
    4: Day4(),
    5: Day5(),
    6: Day6(),
    7: Day7(),
    8: Day8(),
    9: Day9(),
    10: Day10(),
    11: Day11(),
    12: Day12(),
    13: Day13(),
    14: Day14(),
    15: Day15(),
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
        for num, day in days.items():
            print(f'Day {num}')
            get_solutions(day)
            print()
    