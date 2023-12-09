from day import Day


class Day3(Day):

    def __init__(self):
        Day.__init__(self, 3)

    def get_solution_a(self, input_data):
        schematic = input_data
        # remove \n from end of each line
        for row in range(len(schematic) - 1):
            schematic[row] = schematic[row][:-1]
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
        pass
        
    def get_expected_a(self):
        return 4361

    def get_expected_b(self):
        pass