X_real= [l.strip() for l in open('2-input')]
X_test = [l.strip() for l in open('2-input-test')]

X = X_real

max_values = {
    'red': 12,
    'green': 13,
    'blue': 14
}

sum_part_1 = 0
sum_part_2 = 0

for x in X:
    error = False
    raw_input = x.split(': ')
    game_id = raw_input[0].split(' ')[1]
    subsets = raw_input[1].split('; ')

    counter = {
        'red': 0,
        'blue': 0,
        'green': 0
    }

    for s in subsets:
        kubes = s.split(', ')
        for k in kubes:
            colour = k.split(' ')[1]
            number = int(k.split(' ')[0])
            counter[colour] = max(counter[colour], number)
    
    power = 1
    for c, n in counter.items():
        power *= n
        if n > max_values[c]:
            error = True
    sum_part_2 += power

    if error is False:
        sum_part_1 += int(game_id)

print(sum_part_1)
print(sum_part_2)
