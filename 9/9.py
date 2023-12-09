import collections
import re

X_real= [l.strip() for l in open('9-input')]
X_test = [l.strip() for l in open('9-input-test')]

X = X_real

def take_diff(row):
    diff_row = []
    rows = []
    for i in range(len(row) - 1, 0, -1):
        diff_row.append(row[i] - row[i - 1])

    diff_row = list(reversed(diff_row))

    rows.append(diff_row)
    
    if all(v== 0 for v in diff_row):
        return rows 
    else:
        rows.extend(take_diff(diff_row)) 

    return rows
    

part_1_sum = 0
for x in X:
    row = [int(xp) for xp in x.split()]
    diff_list = take_diff(row)
    target_length = len(row) 

    for i in range(len(diff_list) - 1, -1, -1):

        if i == len(diff_list) - 1:
            fill_value = 0
        else:
            fill_value = diff_list[i][-1] + diff_list[i+1][-1]
        
        diff_list[i].append(fill_value)
    
    part_1_sum += fill_value + row[-1]

part_2_sum = 0
for x in X:
    row = [int(xp) for xp in x.split()]
    diff_list = take_diff(row)
    target_length = len(row) 
    
    for i in range(len(diff_list) - 1, -1, -1):
        if i == len(diff_list) - 1:
            fill_value = 0
        else:
            fill_value = diff_list[i][0] - diff_list[i+1][0]
        
        diff_list[i].insert(0, fill_value)
    
    part_2_sum += row[0] - fill_value

print('part 1:', part_1_sum)
print('part 2:', part_2_sum)




