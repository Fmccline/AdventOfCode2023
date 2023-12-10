from day import Day

class Day8(Day):

    def __init__(self):
        Day.__init__(self, 8)

    def get_nodes(self, input_data):
        nodes = {}
        for node in input_data[2:]:
            node_name = node[0:3]
            node_left = node[7:10]
            node_right = node[12:15]
            nodes[node_name] = {'L': node_left, 'R': node_right}
        return nodes

    def get_solution_a(self, input_data):
        # get instructions
        # make map of nodes
        # follow instructions counting steps to take to reach end node
        instructions = input_data[0].replace('\n', '')
        nodes = self.get_nodes(input_data)
        
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
        # get instructions
        # make map of nodes
        # count how many steps A nodes need to get to a Z node
        # find the lowest common multiple between those steps
        instructions = input_data[0].replace('\n', '')
        nodes = self.get_nodes(input_data)
        
        current_nodes = []
        for node in nodes.keys():
            if 'A' in node:
                current_nodes.append(node)

        steps_to_z = []
        for node in current_nodes:
            i_idx = 0
            steps = 0
            while 'Z' not in node:
                instruction = instructions[i_idx]
                node = nodes[node][instruction]
                i_idx = 0 if i_idx + 1 == len(instructions) else i_idx + 1
                steps += 1
            steps_to_z.append(steps)
        steps_to_z.sort(reverse=True)
        return self.compute_lcm(steps_to_z)

    def compute_lcm(self, nums):
        a = nums[0]
        b = nums[1] if len(nums) == 2 else self.compute_lcm(nums[1:])
        gcf = self.compute_gcf(a, b)
        return a * b // gcf        
    
    def compute_gcf(self, a, b):
        gcf = min(a, b)
        is_gcf = False
        while not is_gcf:
            if a % gcf == 0 and b % gcf == 0:
                is_gcf = True
            else:
                is_gcf = False
                gcf -= 1
        return gcf       

    def get_expected_a(self):
        return 6

    def get_expected_b(self):
        return 6