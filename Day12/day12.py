from day import Day

class Day12(Day):

    def __init__(self):
        Day.__init__(self, 12)

    def get_solution_a(self, input_data):
        condition_records = []
        for line in input_data:
            springs = line.split(' ')[0]
            sequence = line.split(' ')[1].replace('\n','').split(',')
            sequence = [int(num) for num in sequence]
            condition_records.append((springs, sequence))
        
        total_arrangements = 0
        arr_list = []
        for record in condition_records:
            springs = record[0]
            sequence = record[1]
            next_cont = self.get_next_contiguous_idx(springs, 0)
            arrangements = self.count_arrangements(springs, next_cont, 0, sequence)
            total_arrangements += arrangements
            arr_list.append(arrangements)
        return total_arrangements


    def count_arrangements(self, springs, start_idx, cont_idx, sequence):
        # base case
        if cont_idx >= len(sequence) or start_idx >= len(springs):
            if self.is_valid_ending(springs, start_idx):
                return cont_idx >= len(sequence)
            else:
                return 0

        spring = springs[start_idx]
        num_arrangements = 0
        if spring == '?' or spring == '#':
            is_cont, idx = self.is_valid_cont_seq(springs, start_idx, sequence[cont_idx])
            if is_cont:
                num_arrangements += self.count_arrangements(springs, idx + 1, cont_idx + 1, sequence)
        if spring == '?' or spring == '.':
            next_cont = self.get_next_contiguous_idx(springs, start_idx + 1)
            num_arrangements += self.count_arrangements(springs, next_cont, cont_idx, sequence)

        return num_arrangements
                
    def is_valid_cont_seq(self, springs, start_idx, cont_num):
        cont = 0
        ends_with_damaged = False
        is_contiguous = False
        idx = start_idx
        for idx in range(start_idx, len(springs)):
            spring = springs[idx]
            if spring == '.' or cont > cont_num:
                return False, 0
            else:
                cont += 1
            if cont == cont_num:
                break
        
        if idx + 1 < len(springs) and springs[idx + 1] == '#':
            while idx < len(springs) - 1:
                if springs[idx + 1] == '#':
                    cont += 1
                    idx += 1
                else:
                    break

        return cont == cont_num, idx + 1


    def is_valid_ending(self, springs, start_idx):
        for spring in springs[start_idx:]:
            if spring == '#':
                return False
        return True

    def get_next_contiguous_idx(self, springs, start_idx):
        for idx in range(start_idx, len(springs)):
            if springs[idx] == '.':
                continue
            else:
                return idx
        return len(springs)

    def get_solution_b(self, input_data):
        pass
        
    def get_expected_a(self):
        return 21

    def get_expected_b(self):
        pass

