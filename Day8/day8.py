from day import Day

class Day8(Day):

    def __init__(self):
        Day.__init__(self, 8)

    def get_solution_a(self, input_data):
        # get instructions
        # make map of nodes
        # follow instructions counting steps to take to reach end node
        instructions = input_data[0].replace('\n', '')
        nodes = {}
        for node in input_data[2:]:
            node_name = node[0:3]
            node_left = node[7:10]
            node_right = node[12:15]
            nodes[node_name] = {'L': node_left, 'R': node_right}
        
        current = 'AAA'
        i_idx = 0
        steps = 0
        while current != 'ZZZ':
            instruction = instructions[i_idx]
            current = nodes[current][instruction]
            i_idx = 0 if i_idx + 1 == len(instructions) else i_idx + 1
            steps += 1
        return steps

    def get_solution_b(self, input_data):
        pass
        
    def get_expected_a(self):
        return 6

    def get_expected_b(self):
        pass