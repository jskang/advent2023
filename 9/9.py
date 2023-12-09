from operator import sub

X_real= [l.strip() for l in open('9-input')]
X_test = [l.strip() for l in open('9-input-test')]

X = X_real

def take_diff(row):
    diff_row = list(map(sub, row[1:], row))

    rows = [diff_row]
    if not all(v== 0 for v in diff_row):
        rows.extend(take_diff(diff_row))
    
    return rows

def get_increment_prediction(diff_list):
    for i in reversed(range(len(diff_list))):
        next = 0
        if i != len(diff_list) - 1:
            next = diff_list[i][-1] + diff_list[i+1][-1]
        
        diff_list[i].append(next)
    
    return next 

part_1_sum = 0
part_2_sum = 0

for x in X:
    row = [int(xp) for xp in x.split()]
    part2_row = list(reversed(row))

    part_1_sum += get_increment_prediction(take_diff(row)) + row[-1]
    part_2_sum += get_increment_prediction(take_diff(part2_row)) + part2_row[-1]

print('part 1:', part_1_sum)
print('part 2:', part_2_sum)
