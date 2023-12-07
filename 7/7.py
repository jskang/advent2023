import collections
X_real= [l.strip() for l in open('7-input')]
X_test = [l.strip() for l in open('7-input-test')]

X = X_real

card_map = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

joker_card_map = card_map.copy()
joker_card_map['J'] = 1

# strength goes from 6 to 0
def get_card_strength(cards):
    card_set = set(cards)
    char_map = collections.defaultdict(int)
    for c in cards:
        char_map[c] += 1

    # high card
    if len(card_set) == 5:
        return 0
    # one pair
    elif len(card_set) == 4:
        return 1
    # two pair and three of a kind
    elif len(card_set) == 3:
        if max(char_map.values()) >= 3:
            return 3
        return 2
    # full house or four of a kind
    elif len(card_set) == 2:
        if max(char_map.values()) >= 4:
            return 5
        return 4
    # five of a kind
    return 6

def joker_converter(cards, card_map):
    if 'J' not in cards: 
        return cards
    
    if 'J' in cards and len(set(cards)) == 1:
        return cards
    
    char_map = collections.defaultdict(int)
    for c in cards:
        char_map[c] += 1   
    
    num_js = char_map.pop('J', 0)

    # Find the max 
    highest_num = max(char_map.values())
    highest_pairs = [k for k,v in char_map.items() if v == highest_num]
    highest_pair_nums = [card_map[p] for p in highest_pairs]    

    to_replace = str(highest_pairs[highest_pair_nums.index(max(highest_pair_nums))])

    new_cards = cards.replace('J', to_replace)

    return(new_cards)
    
def add_to_hand_list(cards, strength, type_list, card_map):
    sub_list = type_list[strength]
    len_sl = len(sub_list)
    replace = False
    if len_sl > 0:
        for i in range(len_sl):
            sorted_cards, _ = sub_list[i] 
            for ci in range(len(sorted_cards)):
                if card_map[sorted_cards[ci]] > card_map[cards[ci]]:
                    break
                elif card_map[cards[ci]] > card_map[sorted_cards[ci]]:
                    replace = True
                    break
            if replace:
                sub_list.insert(i, (cards, bet))
                break
        if replace is False:
            sub_list.append((cards, bet))
    else:
        sub_list.append((old_cards, bet))

type_list_p1 = [[] for i in range(7)]
type_list_p2 = [[] for i in range(7)]

for x in X:
    old_cards, bet = x.split()
    old_strength = get_card_strength(old_cards)

    new_cards = joker_converter(old_cards, card_map)
    new_strength = get_card_strength(new_cards)

    add_to_hand_list(old_cards, old_strength, type_list_p1, card_map)
    add_to_hand_list(old_cards, new_strength, type_list_p2, joker_card_map)

organized_list_p1 = [l for li in type_list_p1 for l in reversed(li) if l]
organized_list_p2 = [l for li in type_list_p2 for l in reversed(li) if l]

part1_sum = 0
part2_sum = 0
for l in range(len(organized_list_p1)):
    rank = l + 1
    part1_sum += int(organized_list_p1[l][1]) * rank
    part2_sum += int(organized_list_p2[l][1]) * rank

print('part1: ', part1_sum)
print('part2: ', part2_sum)