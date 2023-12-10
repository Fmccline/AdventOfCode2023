from day import Day


class Day5(Day):

    def __init__(self):
        Day.__init__(self, 5)

    def get_solution_a(self, input_data):
        # get seeds
        seeds = input_data[0].split(': ')[1].split(' ')
        seeds = [int(seed) for seed in seeds]
        # have a list of lists
        maps = self.get_range_mappings(input_data[3:])
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
        # get seed ranges
        seeds = input_data[0].split(': ')[1].split(' ')
        seeds = [int(seed) for seed in seeds]
        seed_ranges = []
        for seed_idx in range(0, len(seeds) - 1, 2):
            # range of seeds inclusive [start, end]
            seed_range = (seeds[seed_idx], seeds[seed_idx] + seeds[seed_idx+1] - 1)
            seed_ranges.append(seed_range)
        maps = self.get_range_mappings(input_data[3:])
        # go through the ranges and change the seeds to locations through mappings
        for ranges in maps:
            new_ranges = []
            seed_range = seed_ranges.pop()
            x = 0
            while seed_range is not None:
                seed_start = seed_range[0]
                seed_end = seed_range[1]
                for range_num in ranges:
                    # start and end of range [start, end]
                    start = range_num[1]
                    end = range_num[1] + range_num[2] - 1
                    difference = start - range_num[0]
                    # check if whole seed range is in one range
                    if seed_start >= start and seed_end <= end:
                        seed_start -= difference
                        seed_end -= difference
                        break
                    # check if part of beginning of seed range is in one range
                    # add ending back to seed_ranges
                    elif seed_start >= start and seed_start <= end:
                        seed_ranges.append((end + 1, seed_end))
                        seed_start -= difference
                        seed_end = end - difference
                        break
                    # check if part of end in in range
                    # add beginning back to seed_ranges
                    elif start >= seed_start and seed_end <= end and seed_end >= start:
                        seed_ranges.append((seed_start, start - 1))
                        seed_start = start - difference
                        seed_end -= difference
                        break
                    # check if part of middle is in range
                    # add beginning and end back to seed_ranges
                    elif start >= seed_start and seed_end >= start and end < seed_end:
                        seed_ranges.append((seed_start, start - 1))
                        seed_ranges.append((end + 1, seed_end))
                        seed_start = start - difference
                        seed_end = end - difference
                        break
                new_ranges.append((seed_start, seed_end))
                if len(seed_ranges) > 0:
                    seed_range = seed_ranges.pop()
                else:
                    seed_range = None
            seed_ranges = new_ranges
        min_location = min(seed_ranges[0])
        for seed_range in seed_ranges[1:]:
            min_location = min(min(seed_range), min_location)
        return min_location
        
    
    def get_range_mappings(self, input_data):
        # have a list of lists
        maps = []
        # each list has a range tuple mapped to the value to add to the num
        ranges = []
        for line in input_data:
            if line == '\n':
                continue
            elif not line[0].isdigit():
                maps.append(ranges)
                ranges = []
            else:
                nums = [int(num) for num in line.split(' ')]
                ranges.append((nums[0], nums[1], nums[2]))
        maps.append(ranges)
        return maps

    def get_expected_a(self):
        return 35

    def get_expected_b(self):
        return 46