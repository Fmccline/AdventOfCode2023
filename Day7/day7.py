from day import Day

class Day7(Day):

    def __init__(self):
        Day.__init__(self, 7)

    def get_hand_type(self, hand):
        '''
        6 - 5 of a kind
        5 - 4 of a kind
        4 - full house
        3 - 3 of a kind
        2 - two pair
        1 - one pair
        0 - high card
        '''
        cards = {}
        for card in hand:
            if card not in cards.keys():
                cards[card] = 0
            cards[card] += 1
        # 5 of a kind
        if len(cards.keys()) == 1:
            return 6
        # 4 of a kind, full house
        elif len(cards.keys()) == 2:
            if 4 in cards.values():
                return 5
            else:
                return 4
        # 3 of a kind, two pair
        elif len(cards.keys()) == 3:
            if 3 in cards.values():
                return 3
            else:
                return 2
        # one pair
        elif len(cards.keys()) == 4:
            return 1
        # must be high card
        else:
            return 0
        
    def get_hands(self, input_data):
        hands = []
        for line in input_data:
            line = line.split(' ')
            hand = line[0]
            # replace so hand can be sorted later
            hand = hand.replace('A', 'Z')
            hand = hand.replace('K', 'Y')
            hand = hand.replace('Q', 'X')
            hand = hand.replace('J', 'W')
            hand = hand.replace('T', 'V')
            bid = int(line[1])
            hands.append((hand, bid))
        return hands

    def get_solution_a(self, input_data):
        '''
        put hands into types
        sort each type
        combine the types to get rankings
        add up total score
        '''
        hand_types = {}
        for i in range(7):
            hand_types[i] = []

        hands = self.get_hands(input_data)
        for hand in hands:
            hand_type = self.get_hand_type(hand[0])
            hand_types[hand_type].append(hand)

        ranked_hands = []
        for hand_type in range(7):
            hands = hand_types[hand_type]
            if not hands:
                continue
            hands.sort(key=lambda hand: hand[0])
            ranked_hands.extend(hands)

        winnings = 0
        hand_rank = 1
        for rank in range(len(ranked_hands)):
            hand = ranked_hands[rank]
            winnings += hand[1]*(rank+1)

        return winnings


    def get_solution_b(self, input_data):
        pass
        
    def get_expected_a(self):
        return 6440

    def get_expected_b(self):
        pass