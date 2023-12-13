X_real= [l.strip() for l in open('input.txt')]
X_test = [l.strip() for l in open('input-test.txt')]

L = X_real

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
            comp_all = []
            for l, r in zip(left, right):
                comparison = [lc == rc for lc, rc in zip(l, r)]
                comp_all.extend(comparison)
            
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
    columns = []
    for j in range(len(m[0])):
        row = []
        for i in range(len(m)):   
            row.append(m[i][j])
        columns.append(''.join(row))

    part_1 += matcher(columns, 1)
    part_2 += matcher(columns, 1, True)
    
print('part 1:', part_1)
print('part 1:', part_2)