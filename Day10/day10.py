from day import Day
import queue

class Day10(Day):

    def __init__(self):
        Day.__init__(self, 10)

    def get_solution_a(self, input_data):
        start = None
        neighbors = {}
        grid = []
        for line in input_data:
            row = []
            for col in line:
                if col == '\n':
                    continue
                elif col == 'S':
                    start = (len(grid), len(row), 0)
                row.append(col)
            grid.append(row)

        visited = set()
        nodes = queue.Queue()
        nodes.put(start)
        distance = 0
        while not nodes.empty():
            node = nodes.get()
            r = node[0]
            c = node[1]
            d = node[2]
            pipe = grid[r][c]
            neighbors[node] = []
            visited.add((r, c))
            if pipe in "S-J7" and self.is_neighbor(r, c - 1, grid, "-FL"):
                neighbor = (r, c - 1)
                if neighbor not in visited:
                    neighbors[node].append(neighbor)
                    nodes.put((neighbor[0], neighbor[1], d + 1))
            if pipe in "S-FL" and self.is_neighbor(r, c + 1, grid, "-J7"):
                neighbor = (r, c + 1)
                if neighbor not in visited:
                    neighbors[node].append(neighbor)
                    nodes.put((neighbor[0], neighbor[1], d + 1))
            if pipe in "S|LJ" and self.is_neighbor(r - 1, c, grid, "|7F"):
                neighbor = (r - 1, c)
                if neighbor not in visited:
                    neighbors[node].append(neighbor)
                    nodes.put((neighbor[0], neighbor[1], d + 1))
            if pipe in "S|7F" and self.is_neighbor(r + 1, c, grid, "|LJ"):
                neighbor = (r + 1, c)
                if neighbor not in visited:
                    neighbors[node].append(neighbor)
                    nodes.put((neighbor[0], neighbor[1], d + 1))
            if not neighbors[node]:
                return d

    def print_area(self, row, col, grid):
        print(grid[row - 1][col - 1: col + 2])
        print(grid[row][col - 1: col + 2])
        print(grid[row + 1][col - 1: col + 2])

    def is_neighbor(self, row, col, grid, pipes):
        if row < len(grid) and col < len(grid[0]) and row >= 0 and col >= 0:
            return grid[row][col] in pipes
        return False
                
    def get_solution_b(self, input_data):
        pass
        
    def get_expected_a(self):
        return 8

    def get_expected_b(self):
        pass