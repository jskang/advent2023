import collections
X_real= [l.strip() for l in open('4-input')]
X_test = [l.strip() for l in open('4-input-test')]

X = X_real

card_counter = collections.defaultdict(int)
part1_sum = 0
part2_sum = 0

for i in range(len(X)):
    win, number = X[i].split(':')[1].split('|')
    win_set = set(win.split())
    number_set = set(number.split())

    win_count = len(win_set.intersection(number_set))

    # part1: Calculate points
    if win_count:
        part1_sum += pow(2, win_count - 1)

    # part2:
    # Since you're processing the card, you must have one card
    card_counter[i] += 1
    for j in range(win_count):
        win_pos = i + j + 1
        if win_pos < len(X):
            card_counter[win_pos] += card_counter[i]

print(part1_sum)
print(sum(card_counter.values()))