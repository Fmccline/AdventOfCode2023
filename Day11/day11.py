from day import Day

class Day11(Day):

    def __init__(self):
        Day.__init__(self, 11)

    def get_grid(self, input_data):
        grid = []
        for line in input_data:
            row = []
            for space in line.replace('\n', ''):
                row.append(space)
            grid.append(row)
        return grid

    def get_galaxies(self, grid):
        galaxies = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '#':
                    galaxies.append((row, col))
                    grid[row][col] = str(len(galaxies))
        return galaxies

    def get_empty_cols(self, grid):
        empty_cols = []
        for col in range(len(grid[0])):
            is_empty = True
            for row in grid:
                if row[col] == '#':
                    is_empty = False
                    break
            if is_empty:
                empty_cols.append(True)
            else:
                empty_cols.append(False)
        return empty_cols

    def get_empty_rows(self, grid):
        empty_rows = []
        for row in grid:
            if '#' in row:
                empty_rows.append(False)
            else:
                empty_rows.append(True)
        return empty_rows

    def get_distance(self, p1, p2, empty_list, distance):
        d = 0
        start = min(p1, p2)
        end = max(p1, p2)
        for p in range(start, end):
            if empty_list[p] is True:
                d += distance
            else:
                d += 1
        return d

    def get_solution(self, input_data, empty_distance):
        grid = self.get_grid(input_data)
        empty_cols = self.get_empty_cols(grid)
        empty_rows = self.get_empty_rows(grid)
        galaxies = self.get_galaxies(grid)
        
        smallest_distances = 0
        for galaxy_idx in range(len(galaxies) - 1):
            galaxy = galaxies[galaxy_idx]
            for next_idx in range(galaxy_idx + 1, len(galaxies)):
                next_galaxy = galaxies[next_idx]
                y1 = galaxy[0]
                x1 = galaxy[1]
                y2 = next_galaxy[0]
                x2 = next_galaxy[1]
                y_dist = self.get_distance(y1, y2, empty_rows, empty_distance)
                x_dist = self.get_distance(x1, x2, empty_cols, empty_distance)
                smallest_distances += x_dist + y_dist
        return smallest_distances
    
    def get_solution_a(self, input_data):
        return self.get_solution(input_data, 2)

    def get_solution_b(self, input_data):
        return self.get_solution(input_data, 1000000)
        
    def get_expected_a(self):
        return 374

    def get_expected_b(self):
        return 82000210