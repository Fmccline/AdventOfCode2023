from day import Day


class Day6(Day):

    def __init__(self):
        Day.__init__(self, 6)

    def get_records(self, input_data):
        times = []
        for time in input_data[0].split(':')[1].strip().split(' '):
            if time != '':
                times.append(int(time))
        distances = []
        for distance in input_data[1].split(':')[1].strip().split(' '):
            if distance != '':
                distances.append(int(distance))
        return list(zip(times, distances))

    def get_solution_a(self, input_data):
        records = self.get_records(input_data)
        power_win = 1
        for record in records:
            '''
            t = time held = velocity
            T = time of race
            d = distance
            d = t*(T - t)
            '''
            ways_to_win = 0
            T = record[0]
            D = record[1]
            for t in range(T - 1):
                d = t*(T - t)
                if d > D:
                    ways_to_win += 1
            power_win *= ways_to_win
        return power_win

    def get_solution_b(self, input_data):
        pass
        
    def get_expected_a(self):
        return 288

    def get_expected_b(self):
        pass