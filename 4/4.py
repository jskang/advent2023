import collections
X_real= [l.strip() for l in open('4-input')]
X_test = [l.strip() for l in open('4-input-test')]

X = X_real

card_counter = collections.defaultdict(int)
part1_sum = 0

for i in range(len(X)):
    win, number = X[i].split(':')[1].split('|')
    win = win.split()
    number = number.split()

    win_set = set(win)
    num_set = set(number)
    winning_numbers = win_set.intersection(num_set)

    # Calculate points for part 1
    points = 0
    if len(winning_numbers):
        points = pow(2, len(winning_numbers) - 1)

    # Since you're processing the card, you must have one card
    card_counter [i] += 1
    for j in range(len(winning_numbers)):
        win_pos = i + j + 1
        if win_pos < len(X):
            card_counter[win_pos] += card_counter[i]
    
    part1_sum += points 

print(part1_sum)

part2_sum = 0
for k,v in card_counter.items():
    part2_sum += v 

print(part2_sum)