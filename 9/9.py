from operator import sub

X_real= [l.strip() for l in open('9-input')]
X_test = [l.strip() for l in open('9-input-test')]

X = X_real

def get_prediction(row):
    if not any(row):
        return 0
    diff_row = list(map(sub, row[1:], row))
    return row[-1] + get_prediction(diff_row)

part_1_sum = 0
part_2_sum = 0

for x in X:
    row = [int(xp) for xp in x.split()]
    part2_row = list(reversed(row))

    part_1_sum += get_prediction(row)
    part_2_sum += get_prediction(part2_row)

print('part 1:', part_1_sum)
print('part 2:', part_2_sum)
