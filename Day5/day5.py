from day import Day


class Day5(Day):

    def __init__(self):
        Day.__init__(self, 5)

    def get_solution_a(self, input_data):
        # get seeds
        seeds = input_data[0].split(': ')[1].split(' ')
        seeds = [int(seed) for seed in seeds]
        # have a list of lists
        maps = []
        # each list has a range tuple mapped to the value to add to the num
        ranges = []
        for line in input_data[3:]:
            if line == '\n':
                continue
            elif not line[0].isdigit():
                maps.append(ranges)
                ranges = []
            else:
                nums = [int(num) for num in line.split(' ')]
                ranges.append((nums[0], nums[1], nums[2]))
        maps.append(ranges)
        # go through the ranges and change the seeds to locations through mappings
        for ranges in maps:
            for seed_idx in range(len(seeds)):
                seed = seeds[seed_idx]
                for range_num in ranges:
                    start = range_num[1]
                    end = range_num[1] + range_num[2]
                    if seed >= start and seed < end:
                        new_seed = seed - (range_num[1] - range_num[0])
                        seeds[seed_idx] = new_seed
                        break
        return min(seeds)

    def get_solution_b(self, input_data):
        pass
        
    def get_expected_a(self):
        return 35

    def get_expected_b(self):
        pass