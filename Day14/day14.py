from day import Day

class Day14(Day):

    def __init__(self):
        Day.__init__(self, 14)

    def get_solution_a(self, input_data):
        grid = []
        for line in input_data:
            line = line.replace('\n', '')
            row = []
            for char in line:
                row.append(char)
            grid.append(row)
        
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                if grid[row_idx][col_idx] == 'O':
                    self.roll_north(row_idx, col_idx, grid)

        total_load = 0
        for row_idx in range(len(grid)):
            row = grid[row_idx]
            total_load += row.count('O')*(len(grid) - row_idx)
        return total_load
                
                
    def roll_north(self, row, col, grid):
        if row > 0:
            if grid[row - 1][col] == '.':
                grid[row - 1][col] = 'O'
                grid[row][col] = '.'
                self.roll_north(row - 1, col, grid)

    def get_solution_b(self, input_data):
        pass

    def get_expected_a(self):
        return 136

    def get_expected_b(self):
        return 64