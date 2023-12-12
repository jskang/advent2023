import itertools
import math

X_real= [l.strip() for l in open('input.txt')]
X_test = [l.strip() for l in open('input-test.txt')]

L = X_real

# find_expansion
# Expand graph
# find galaxies find distance
expansion_row = []
expansion_col = []

# find the rows that need to be expanded
for i in range(len(L)):
    count = 0
    row = set(L[i])
    if len(row) == 1 and '.' in row:
        expansion_row.append(i)

# find the cols that need to be expanded
for j in range(len(L[0])):
    l = []
    for i in range(len(L)):
        l.append(L[i][j])
    
    row = set(l)
    if len(row) == 1 and '.' in row:
        expansion_col.append(j)

# get the coordinates for the galaxies
pre_map = []
for y in range(len(L)):
    for x in range(len(L[i])):
        if L[y][x] == '#':
            pre_map.append((x, y))


def calculate_expansion(diff, coord1, coord2, multiplier, expansion_list):
    if diff == 0:
        return 0 

    n_expansion = 0
    sign = diff//abs(diff)
    for i in range(coord1, coord2, sign):
        if i in expansion_list:
            n_expansion += sign * multiplier - sign
    
    return n_expansion 
    

def calculate_distance(pre_map, multiplier):
    total = 0
    # Create combinations
    for start, end in itertools.combinations(pre_map, 2):
        x1, y1 = start
        x2, y2 = end

        x_diff = x2 - x1
        y_diff = y2 - y1

        x_diff += calculate_expansion(x_diff, x1, x2, multiplier, expansion_col)
        y_diff += calculate_expansion(y_diff, y1, y2, multiplier, expansion_row)

        total += abs(x_diff) + abs(y_diff)

    return total

# Technically the first part is expansion multipler of 2
print('part1', calculate_distance(pre_map, 2))
print('part2', calculate_distance(pre_map, 1000000))
