import collections

X_real= [l.strip() for l in open('3-input')]
X_test = [l.strip() for l in open('3-input-test')]

X = X_real

# [x, y]
tests = [[1,-1], [1,0], [1,1],
         [0,-1],          [0,1],
         [-1,-1], [-1, 0], [-1,1]]

def CheckSymbol(X, i, j):
    for t in tests:
        i_test = i + t[0]
        j_test = j + t[1]

        if i_test < 0 or i_test >= len(X) or j_test < 0 or j_test >= len(X[i]):
            continue

        test_value = X[i_test][j_test]

        if not test_value.isdigit() and test_value != '.':
            return True

    return False

def GetStarLocation(X, i, j):
    star_list = []
    for t in tests:
        i_test = i + t[0]
        j_test = j + t[1]

        if i_test < 0 or i_test >= len(X) or j_test < 0 or j_test >= len(X[i]):
            continue

        test_value = X[i_test][j_test]

        if test_value == '*':
            star_list.append((i_test, j_test))

    return star_list


gear_map = collections.defaultdict(list)
total_part_1 = 0
total_part_2 = 0

for i in range(len(X)):
    number = ''
    valid = False
    gear_list = []

    # Run the loop one more time to cover cases where the row ends with a number
    # Add length check before indexing with `and` to prevent index out of bounds
    # Keep the numbers as string
    for j in range(len(X[i]) + 1):
        if j < len(X[i]) and X[i][j].isdigit():
            number += X[i][j]

            if CheckSymbol(X, i, j) is True:
                valid = True
            
            for g in GetStarLocation(X, i, j):
                gear_list.append(g)

        elif number:
            if valid:
                total_part_1 += int(number)

            for s in set(gear_list):
                gear_map[s].append(int(number))           

            number = ''
            valid = False
            gear_list = []

for k, v in gear_map.items():
    if len(v) == 2:
        total_part_2 += v[0] * v[1]

print(total_part_1)
print(total_part_2)