import collections
X_real= [l.strip() for l in open('7-input')]
X_test = [l.strip() for l in open('7-input-test')]

X = X_real

card_map = {x: i for i, x in enumerate("AKQJT98765432")}
joker_map = {x: i for i, x in enumerate("AKQT98765432J")}

# strength goes from 6 to 0
def get_card_strength(cards):
    card_set = set(cards)
    char_map = collections.defaultdict(int)
    chars = collections.Counter(cards)

    # high card
    if len(card_set) == 5:
        return 0
    # one pair
    elif len(card_set) == 4:
        return 1
    # two pair and three of a kind
    elif len(card_set) == 3:
        if max(chars.values()) == 3:
            return 3
        return 2
    # full house or four of a kind
    elif len(card_set) == 2:
        if max(chars.values()) == 4:
            return 5
        return 4
    # five of a kind
    return 6

def joker_converter(cards, card_map):
    if 'J' not in cards: 
        return cards
    
    if 'J' in cards and len(set(cards)) == 1:
        return cards
    
    chars = collections.Counter(cards)
    
    del chars['J']
    # Find the max 
    list_of_pairs = chars.most_common(1)
    highest_pairs = [(card_map[k], k) for k, _ in list_of_pairs]
    to_replace = sorted(highest_pairs)[0][1]

    new_cards = cards.replace('J', to_replace)

    return(new_cards)
    
# 7 types of hands are present
type_list_p1 = [[] for i in range(7)]
type_list_p2 = [[] for i in range(7)]

for x in X:
    old_cards, bet = x.split()
    old_strength = get_card_strength(old_cards)

    new_cards = joker_converter(old_cards, joker_map)
    new_strength = get_card_strength(new_cards)

    # Part 1
    normal_map_values = [card_map[c] for c in old_cards]
    type_list_p1[old_strength].append((normal_map_values, bet))

    # Part 2
    joker_map_values = [joker_map[c] for c in old_cards]
    type_list_p2[new_strength].append((joker_map_values, bet))

organized_list_p1 = [l for li in type_list_p1 for l in sorted(li, reverse=True) if l]
organized_list_p2 = [l for li in type_list_p2 for l in sorted(li, reverse=True) if l]

part1_sum = 0
part2_sum = 0
for l in range(len(organized_list_p1)):
    rank = l + 1
    part1_sum += int(organized_list_p1[l][1]) * rank
    part2_sum += int(organized_list_p2[l][1]) * rank

print('part1: ', part1_sum)
print('part2: ', part2_sum)