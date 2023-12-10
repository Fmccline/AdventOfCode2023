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
        if 5 in cards.values():
            return 6
        # 4 of a kind
        elif 4 in cards.values():
            return 5
        # full house, 3 of a kind
        elif 3 in cards.values():
            if 2 in cards.values():
                return 4
            else:
                return 3
        # 2 pair, 1 pair
        elif 2 in cards.values():
            pairs = 0
            for value in cards.values():
                if value == 2:
                    pairs += 1
            return pairs # 2 or 1
        # must be high card
        else:
            return 0

    def get_hand_type_with_wild(self, hand):
        cards = {}
        wilds = 0
        for card in hand:
            if card == '1':
                wilds += 1

        hand_type = self.get_hand_type(hand.replace('1',''))
        best_hands = {
            1: {
                # 5 -> 6 : 4 kind -> 5 kind
                # 4 -> 5 : full house -> 4 of a kind
                # 3 -> 5 : 3 kind -> 4 kind
                # 2 -> 4 : 2 pair -> full house
                # 1 -> 3 : 1 pair -> 3 kind
                # 0 -> 1 : high -> 1 pair
                5 : 6,
                4 : 5,
                3 : 5,
                2 : 4,
                1 : 3,
                0 : 1
            }, 
            2: {
                # 3 -> 6 : 3 kind -> 5 kind
                # 1 -> 4 : 1 pair -> 4 kind
                # 0 -> 3 : high -> 3 kind
                3 : 6,
                1 : 5,
                0 : 3
            },
            3: {
                # 1 -> 6 : 1 pair -> 5 kind
                # 0 -> 5 : high -> 4 kind
                1 : 6,
                0 : 5,
            },
            4: {
                0 : 6
            },
            5: {
                0 : 6
            }
        }
        if wilds == 0:
            return hand_type
        else:
            return best_hands[wilds][hand_type]
            
        return hand_type
        
        
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
        hand_types = {}
        for i in range(7):
            hand_types[i] = []
        hands = self.get_hands(input_data)
        for idx in range(len(hands)):
            hand = hands[idx][0]
            hand = hand.replace('W', '1')
            hands[idx] = (hand, hands[idx][1])
        for hand in hands:
            hand_type = self.get_hand_type_with_wild(hand[0])
            hand_types[hand_type].append(hand)
        ranked_hands = []
        for hand_type in range(7):
            hands = hand_types[hand_type]
            if not hands:
                continue
            hands.sort(key=lambda hand: hand[0])
            ranked_hands.extend(hands)
        winnings = 0
        for rank in range(len(ranked_hands)):
            hand = ranked_hands[rank]
            winnings += hand[1]*(rank+1)
        return winnings        


    def get_expected_a(self):
        return 6440

    def get_expected_b(self):
        return 5905
