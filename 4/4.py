import collections
X_real= [l.strip() for l in open('4-input')]
X_test = [l.strip() for l in open('4-input-test')]

X = X_real

card_counter = collections.defaultdict(int)
part1_sum = 0

for i in range(len(X)):
    win, number = X[i].split(':')[1].split('|')
    win = [w.strip() for w in win.strip().split(' ') if w]
    number = [n.strip() for n in number.strip().split(' ') if n ]

    win_set = set(win)
    num_set = set(number)

    winning_num = win_set.intersection(num_set)
    points = 0

    # Calculate points
    for j in range(len(winning_num)):
        if j == 0:
            points = 1
        else:
            points *= 2
    
    # Since you're processing the card, you must have one card
    card_counter [i] += 1

    for s in range(len(winning_num)):
        win_pos = i + s + 1
        if win_pos < len(X):
            card_counter[win_pos] += card_counter[i]
    
    part1_sum += points 

part2_sum = 0
for k,v in card_counter.items():
    part2_sum += v 

print(part1_sum)
print(part2_sum)