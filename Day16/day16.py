from day import Day

class Day16(Day):

    def __init__(self):
        Day.__init__(self, 16)

    def change_direction(self, direction, mirror):
        reflections = {
            '/': {
                (0, 1): (-1, 0),
                (0, -1): (1, 0),
                (1, 0): (0, -1),
                (-1, 0): (0, 1)
            },
            '\\': {
                (0, 1): (1, 0),
                (0, -1): (-1, 0),
                (1, 0): (0, 1),
                (-1, 0): (0, -1)
            }
        }
        return reflections[mirror][direction]

    def energize_beam_path(self, grid, energized, start, direction, visited_paths):
        MAX_ROWS = len(grid)
        MAX_COLS = len(grid[0])
        row = start[0]
        col = start[1]
        while col < MAX_COLS and row < MAX_ROWS and row >= 0 and col >= 0:
            path = (row, col, direction[0], direction[1])
            if path in visited_paths:
                return
            visited_paths.add(path)
            energized[row][col] = 1
            spot = grid[row][col]
            if spot == '-' and direction[0] != 0:
                start = (row, col)
                self.energize_beam_path(grid, energized, start, (0, -1), visited_paths)
                self.energize_beam_path(grid, energized, start, (0, 1), visited_paths)
                return
            elif spot == '|' and direction[1] != 0:
                start = (row, col)
                self.energize_beam_path(grid, energized, start, (1, 0), visited_paths)
                self.energize_beam_path(grid, energized, start, (-1, 0), visited_paths)
                return
            elif spot == '/' or spot == '\\':
                direction = self.change_direction(direction, spot)
            row += direction[0]
            col += direction[1]


    def get_total_energized(self, grid, start, direction):
        energized = []

        for row in grid:
            energized_row = [0 for _ in row]
            energized.append(energized_row)

        self.energize_beam_path(grid, energized, start, direction, set())
        total_energized = 0
        for row in energized:
            total_energized += sum(row)
        
        return total_energized


    def get_solution_a(self, input_data):
        grid = []
        for line in input_data:
            grid.append(line.replace('\n', ''))
        return self.get_total_energized(grid, (0, 0), (0, 1))


    def get_solution_b(self, input_data):
        grid = []
        for line in input_data:
            grid.append(line.replace('\n', ''))
        
        MAX_ROWS = len(grid)
        MAX_COLS = len(grid[0])

        edges = []
        # add top and bottom edges
        for col in range(0, MAX_COLS):
            edges.append(((0, col), (1, 0)))
            edges.append(((MAX_ROWS - 1, col), (-1, 0)))
        # add left and right edges
        for row in range(0, MAX_ROWS):
            edges.append(((row, 0), (0, 1)))
            edges.append(((row, MAX_COLS - 1), (0, -1)))
        
        max_energized = 0
        for edge in edges:
            start = edge[0]
            direction = edge[1]
            total_energized = self.get_total_energized(grid, start, direction)
            max_energized = max(max_energized, total_energized)
        return max_energized
        
    def get_expected_a(self):
        return 46

    def get_expected_b(self):
        return 51