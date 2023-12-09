from day import Day


class Day3(Day):

    def __init__(self):
        Day.__init__(self, 3)

    def get_solution_a(self, input_data):
        schematic = input_data
        # scan for a number
        # get full length of number
        # for each digit
        #   check each neighbor of number for a symbol
        parts_sum = 0
        row, start_col, end_col = self.scan_number(0, 0, schematic)
        while row is not None:
            if self.is_part_number(row, start_col, end_col, schematic):
                part_num = int(schematic[row][start_col:end_col+1])
                parts_sum += part_num
            row, start_col, end_col = self.scan_number(row, end_col+1, schematic)
        return parts_sum

    def scan_number(self, row, col, schematic):
        while row < len(schematic):
            while col < len(schematic[row]):
                char = schematic[row][col]
                if char.isdigit():
                    # get full number range
                    start_col, end_col = self.get_number(row, col, schematic)
                    return row, start_col, end_col
                col += 1
            row += 1
            col = 0
        return None, None, None
  
    def get_number(self, row, start_col, schematic):
        num = ''
        col = start_col + 1
        while col < len(schematic[row]):
            letter = schematic[row][col]
            if letter.isdigit():
                num += letter
            else:
                break
            col += 1
        col = col-1
        return start_col, col

    def is_part_number(self, row, start_col, end_col, schematic):
        col = start_col
        # check left and left diagonals
        points = [(row, col - 1), (row - 1, col - 1), (row + 1, col - 1)]
        # check above and below
        for col in range(start_col, end_col + 1):
            points.extend([(row - 1, col), (row + 1, col)])
        # check right and right diagonals
        points.extend([(row, end_col + 1), (row - 1, end_col + 1), (row + 1, end_col + 1)])
        return self.points_contain_symbol(points, schematic)

    def points_contain_symbol(self, points, schematic):
        has_symbol = False
        for row, col in points:
            if row >= len(schematic) or col >= len(schematic[row]) or row < 0 or col < 0:
                continue
            elif schematic[row][col].isalpha() or schematic[row][col].isdigit() or schematic[row][col] == '.':
                continue
            else:
                has_symbol = True
                break
        return has_symbol

    def get_solution_b(self, input_data):
        gear_ratios = 0
        schematic = input_data
        numbers, potential_gears = self.get_numbers_and_potential_gears(schematic)
        for row, col in potential_gears:
            gears = []
            # top mid
            point = (row - 1, col)
            if point in numbers.keys():
                gears.append(numbers[point])
            # else check top left and right
            else:
                points = [(row - 1, col - 1), (row - 1, col + 1)]
                gears = self.check_for_gears(points, numbers, gears)
            # bottom mid
            point = (row + 1, col)
            if point in numbers.keys():
                gears.append(numbers[point])
            # bottom left and right
            else:
                points = [(row + 1, col - 1), (row + 1, col + 1)]
                gears = self.check_for_gears(points, numbers, gears)
            # left and right
            points = [(row, col - 1), (row, col + 1)]
            gears = self.check_for_gears(points, numbers, gears)
            if len(gears) == 2:
                gear_ratios += gears[0] * gears[1]
        return gear_ratios
    

    def check_for_gears(self, points, numbers, gears):
        for point in points:
            if point in numbers.keys():
                gears.append(numbers[point])
        return gears


    def get_numbers_and_potential_gears(self, schematic):
        numbers = {}
        potential_gears = []
        row = 0
        while row < len(schematic):
            col = 0
            while col < len(schematic[row]):
                char = schematic[row][col]
                if char.isdigit():
                    start_col, end_col = self.get_number(row, col, schematic)
                    num = int(schematic[row][start_col:end_col+1])
                    for num_col in range(start_col, end_col + 1):
                        numbers[(row, num_col)] = num
                    col = end_col
                elif char == '*':
                    potential_gears.append((row, col))
                col += 1
            row += 1
        return numbers, potential_gears
        
    def get_expected_a(self):
        return 4361

    def get_expected_b(self):
        return 467835