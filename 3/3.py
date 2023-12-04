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
    gear_list = []
    for t in tests:
        i_test = i + t[0]
        j_test = j + t[1]

        if i_test < 0 or i_test >= len(X) or j_test < 0 or j_test >= len(X[i]):
            continue

        test_value = X[i_test][j_test]

        if test_value == '*':
            gear_list.append((i_test, j_test))

    return gear_list


gear_map = collections.defaultdict(list)
total_part_1 = 0
total_part_2 = 0

for i in range(len(X)):
    skip_counter = 0
    for j in range(len(X[i])):
        if skip_counter > 0:
            skip_counter -= 1
            continue 

        if X[i][j].isdigit():
            j_search = j 
            number = ''
            valid = False
            gear_list = list()

            # If a number is found go to the end of the number and process everything all at once
            while j_search < len(X[i]) and X[i][j_search].isdigit():
                if CheckSymbol(X, i, j_search) is True:
                    valid = True

                for g in GetStarLocation(X, i, j_search):
                    gear_list.append(g)

                number = number + X[i][j_search]

                skip_counter += 1
                j_search += 1

            if valid:
                total_part_1 += int(number)

            for s in set(gear_list):
                gear_map[s].append(int(number))           

for k, v in gear_map.items():
    if len(v) == 2:
        total_part_2 += v[0] * v[1]

print(total_part_1)
print(total_part_2)