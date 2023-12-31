from day import Day

class Day13(Day):

    def __init__(self):
        Day.__init__(self, 13)

    def is_mirrored(self, rows, top_row, bottom_row):
        # base case
        if top_row < 0 or bottom_row >= len(rows):
            return True
        
        for idx in range(len(rows[top_row])):
            top = rows[top_row][idx]
            bot = rows[bottom_row][idx]
            if top != bot:
                return False

        return self.is_mirrored(rows, top_row - 1, bottom_row + 1)

    def is_mirrored_one_diff(self, rows, top_row, bottom_row, current_diff):
        # base case
        if top_row < 0 or bottom_row >= len(rows):
            return current_diff == 1
        
        for idx in range(len(rows[top_row])):
            top = rows[top_row][idx]
            bot = rows[bottom_row][idx]
            if top != bot:
                current_diff += 1
        
        if current_diff > 1:
            return False
        else:
            return self.is_mirrored_one_diff(rows, top_row - 1, bottom_row + 1, current_diff)

    def get_grids(self, input_data):
        grids = []
        rows = []
        for line in input_data:
            if line == '\n':
                grids.append(rows)
                rows = []
            else:
                line = line.replace('\n', '')
                rows.append(line)
        grids.append(rows)
        
        for grid_idx in range(len(grids)):
            rows = grids[grid_idx]
            cols = []
            for row_idx in range(len(rows[0])):
                col = []
                for row in rows:
                    col.append(row[row_idx])
                cols.append(col)
            grids[grid_idx] = (rows, cols)
        return grids

    def get_solution_a(self, input_data):
        grids = self.get_grids(input_data)
        reflection_sum = 0
        for rows, cols in grids:
            for idx in range(1, len(rows)):
                if self.is_mirrored(rows, idx - 1, idx):
                    reflection_sum += 100*idx
            
            for idx in range(1, len(cols)):
                if self.is_mirrored(cols, idx - 1, idx):
                    reflection_sum += idx
        return reflection_sum

    def get_solution_b(self, input_data):
        grids = self.get_grids(input_data)
        reflection_sum = 0
        for rows, cols in grids:
            for idx in range(1, len(rows)):
                if self.is_mirrored_one_diff(rows, idx - 1, idx, 0):
                    reflection_sum += 100*idx
            
            for idx in range(1, len(cols)):
                if self.is_mirrored_one_diff(cols, idx - 1, idx, 0):
                    reflection_sum += idx

        return reflection_sum
        
    def get_expected_a(self):
        return 405

    def get_expected_b(self):
        return 400