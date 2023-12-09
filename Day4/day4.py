from day import Day


class Day4(Day):

    def __init__(self):
        Day.__init__(self, 4)

    def get_solution_a(self, input_data):
        points = 0
        for card in input_data:
            nums = card.split(':')[1].split(' | ')
            winning_nums = nums[0].strip().split(' ')
            drawn_nums = nums[1].strip().split(' ')
            winners = set()
            total_won = 0
            for num in winning_nums:
                if num == '':
                    continue
                winners.add(int(num))
            for num in drawn_nums:
                if num == '':
                    continue
                num = int(num)
                if num in winners:
                    total_won += 1
            if total_won > 0:
                points += pow(2, total_won - 1)
        return points
        

    def get_solution_b(self, input_data):
        pass
        
    def get_expected_a(self):
        return 13

    def get_expected_b(self):
        pass