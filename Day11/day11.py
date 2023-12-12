from day import Day

class Day11(Day):

    def __init__(self):
        Day.__init__(self, 11)

    def get_solution_a(self, input_data):
        # find empty rows and expand
        grid = []
        for line in input_data:
            line = line.replace('\n', '')
            if '#' not in line:
                grid.append(line)
            grid.append(line)

        # find empty columns and expand
        empty_cols = set()
        for col in range(len(grid[0])):
            is_empty = True
            for row in grid:
                if row[col] == '#':
                    is_empty = False
                    break
            if is_empty:
                empty_cols.add(col)

        new_grid = []
        for row in grid:
            new_row = []
            for col in range(len(row)):
                space = row[col]
                if col in empty_cols:
                    new_row.append('.')
                new_row.append(space)
            new_grid.append(new_row)

        grid = new_grid

        # find galaxies in grid
        galaxies = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '#':
                    galaxies.append((row, col))
                    grid[row][col] = str(len(galaxies))
        
        # go through galaxies and find shortest path between each pair
        shortest_paths = []
        for galaxy_idx in range(len(galaxies) - 1):
            galaxy = galaxies[galaxy_idx]
            for next_idx in range(galaxy_idx + 1, len(galaxies)):
                next_galaxy = galaxies[next_idx]
                x_dist = abs(galaxy[0] - next_galaxy[0]) 
                y_dist = abs(galaxy[1] - next_galaxy[1])
                shortest_paths.append(x_dist + y_dist)

        return sum(shortest_paths)

    def get_solution_b(self, input_data):
        pass
        
    def get_expected_a(self):
        return 374

    def get_expected_b(self):
        pass