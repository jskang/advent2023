import collections
X_real= [l.strip() for l in open('7-input')]
X_test = [l.strip() for l in open('7-input-test')]

X = X_real

card_map = {x: i for i, x in enumerate(reversed("AKQJT98765432"))}
joker_map = {x: i for i, x in enumerate(reversed("AKQT98765432J"))}

# strength goes from 0(High) to 6(Five of a kind)
# Could be replaced by some entropy metric, the higher the entropy the lower the hand
# We don't need to know what the hand is, we only need to know their relative strength
def get_card_strength(cards):
    chars = collections.Counter(cards)
    num_labels = len(chars)

    # high card
    if num_labels == 5:
        return 0
    # one pair
    elif num_labels == 4:
        return 1
    # two pair and three of a kind
    elif num_labels == 3:
        if max(chars.values()) == 3:
            return 3
        return 2
    # full house or four of a kind
    elif num_labels == 2:
        if max(chars.values()) == 4:
            return 5
        return 4
    # five of a kind
    return 6

def joker_converter(cards, card_map):
    if 'J' not in cards: 
        return cards
    
    chars = collections.Counter(cards)

    if 'J' in cards and len(chars) == 1:
        return cards
    
    del chars['J']
    # Find the cards with the most occurences
    list_of_pairs = chars.most_common(1)
    # Map card label a strength/map
    max_num_label = [(card_map[k], k) for k, _ in list_of_pairs]
    # Sort it and pick the highest label card
    to_replace = sorted(max_num_label)[0][1]

    new_cards = cards.replace('J', to_replace)

    return new_cards
    
# 7 types of hands are present
type_list_p1 = []
type_list_p2 = []

for x in X:
    cards, bet = x.split()
    original_strength = get_card_strength(cards)

    joker_cards = joker_converter(cards, joker_map)
    new_strength = get_card_strength(joker_cards)

    # Part 1
    normal_map_values = [card_map[c] for c in cards]
    type_list_p1.append((original_strength, normal_map_values, bet))

    # Part 2
    joker_map_values = [joker_map[c] for c in cards]
    type_list_p2.append((new_strength, joker_map_values, bet))
    
for i, tl in enumerate([type_list_p1, type_list_p2]):
    part_sum = 0
    organized_list = sorted(tl)
    for l in range(len(organized_list)):
        rank = l + 1
        part_sum += int(organized_list[l][-1]) * rank

    print('part{}: '.format(i + 1), part_sum)
    