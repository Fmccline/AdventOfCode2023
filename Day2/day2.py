from util import read_file_to_list
from day import Day


class Day2(Day):

    def __init__(self):
        Day.__init__(self, 2)


    def get_score(self, game):
        score = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        subsets = game.split(':')[1].split(';')
        for subset in subsets:
            revealed_cubes = subset.split(',')
            for revealed_cube in revealed_cubes:
                revealed_cube = revealed_cube.strip().split(' ')
                num = int(revealed_cube[0])
                color = revealed_cube[1]
                score[color] = max(score[color], num)
        return score


    def get_solution_a(self, input_data):
        # get: game_id
        # check each subset and compare to max counts of red, green, blue
        ids_sum = 0
        for game in input_data:
            game_id = int(game.split(':')[0].split(' ')[1])
            score = self.get_score(game)
            if score['red'] <= 12 and score['green'] <= 13 and score['blue'] <= 14:
                ids_sum += game_id
        return ids_sum

    def get_solution_b(self, input_data):
        power_sum = 0
        for game in input_data:
            score = self.get_score(game)
            power_sum += score['red'] * score['green'] * score['blue']
        return power_sum
        
    def get_expected_a(self):
        return 53

    def get_expected_b(self):
        return 2286

