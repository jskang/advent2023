X_real = [l.strip() for l in open('input.txt')]
X_test = [l.strip() for l in open('input-test.txt')]

L = X_real

# Need to find a cleaner way to parse the double line input
maps = []
sub_map = []
for l in L:
    if not l:
        maps.append(sub_map)
        sub_map = []
        continue
    sub_map.append(l)
maps.append(sub_map)

def matcher(m, multiplier, part2=False):
    points = 0
    for i in range(1, len(m), 1):
        check_range = i if i < len(m) - i else len(m) - i
        left = m[i-check_range:i][::-1] 
        right = m[i:i+check_range]

        if part2:
            # Only one smudge needs to be fixed, the two images should only contain one difference
            # We don't care where the smudge is, just that there is one
            comp_all = [lc == rc for l, r in zip(left, right) for lc, rc in zip(l, r)]

            if len(comp_all) - sum(comp_all) == 1:
                points += i * multiplier
        else:
            if left == right:
                points += i * multiplier

    return points

part_1 = 0
part_2 = 0

for m in maps:
    part_1 += matcher(m, 100)
    part_2 += matcher(m, 100, True)

    # flip row and columns
    # columns = list(map(list, zip(*m)))
    columns = [*zip(*m)]

    part_1 += matcher(columns, 1)
    part_2 += matcher(columns, 1, True)
    
print('part 1:', part_1)
print('part 2:', part_2)