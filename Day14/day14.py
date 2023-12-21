from day import Day

class Day14(Day):

    def __init__(self):
        Day.__init__(self, 14)

    def get_solution_a(self, input_data):
        grid = self.get_grid(input_data)        
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                if grid[row_idx][col_idx] == 'O':
                    self.roll_north(row_idx, col_idx, grid)

        return self.count_load(grid)
    
    def get_solution_b(self, input_data):
        grid = self.get_grid(input_data)
        rocks = []
        loads = []
        for idx in range(100):
            # roll north
            for row_idx in range(len(grid)):
                for col_idx in range(len(grid[0])):
                    if grid[row_idx][col_idx] == 'O':
                        self.roll_north(row_idx, col_idx, grid)
            # roll west
            for row_idx in range(len(grid)):
                for col_idx in range(len(grid[0])):
                    if grid[row_idx][col_idx] == 'O':
                        self.roll_west(row_idx, col_idx, grid)
            # roll south
            for row_idx in range(len(grid) - 1, -1, -1):
                for col_idx in range(len(grid[0])):
                    if grid[row_idx][col_idx] == 'O':
                        self.roll_south(row_idx, col_idx, grid)
            # roll east
            for row_idx in range(len(grid)):
                for col_idx in range(len(grid[0]) - 1, -1, -1):
                    if grid[row_idx][col_idx] == 'O':
                        self.roll_east(row_idx, col_idx, grid)
            total_load = self.count_load(grid)
            if total_load == 64:
                print(idx)
            loads.append((idx, total_load))
        for load in loads:
            print(load)
        return 0


    def print_grid(self, grid):
        for row in grid:
            print(''.join(row))

    def get_grid(self, input_data):
        grid = []
        for line in input_data:
            line = line.replace('\n', '')
            row = []
            for char in line:
                row.append(char)
            grid.append(row)
        return grid
    
    def count_load(self, grid):
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
    
    def roll_south(self, row, col, grid):
        if row < len(grid) - 1:
            if grid[row + 1][col] == '.':
                grid[row + 1][col] = 'O'
                grid[row][col] = '.'
                self.roll_south(row + 1, col, grid)

    def roll_east(self, row, col, grid):
        if col < len(grid[0]) - 1:
            if grid[row][col + 1] == '.':
                grid[row][col + 1] = 'O'
                grid[row][col] = '.'
                self.roll_east(row, col + 1, grid)
    
    def roll_west(self, row, col, grid):
        if col > 0:
            if grid[row][col - 1] == '.':
                grid[row][col - 1] = 'O'
                grid[row][col] = '.'
                self.roll_west(row, col - 1, grid)

    def get_expected_a(self):
        return 136

    def get_expected_b(self):
        return 64