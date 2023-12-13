from operator import sub
import collections
import itertools
import re
import copy
from functools import lru_cache

X_real= [l.strip() for l in open('input.txt')]
X_test = [l.strip() for l in open('input-test.txt')]

L = X_test

def checker(spring_map, group):
    broken = re.findall('#+', spring_map)
    output = [len(b) for b in broken]
    # print(broken, output, group, spring_map)
    if output != group:
        return False
    
    return True


# part1_sum = 0
# for l in L:
#     spring_map, c = l.split()
#     groups = [int(x) for x in c.split(',')]

#     # unknowns = re.findall('[?#]+', spring_map)

#     n_knowns = len(re.findall('[#]', spring_map))

#     loc_unknowns = [match.start() for match in re.finditer('[?]', spring_map)]
#     brute_force = sum(groups) - n_knowns

#     for loc in itertools.combinations(loc_unknowns, brute_force):
#         test_map = [c for c in spring_map]
#         for i in loc:
#             test_map[int(i)] = '#'
#         if checker(''.join(test_map), groups):
#             part1_sum += 1

@lru_cache
def get_count(spring_map, groups, loc_unknowns):
    n_knowns = len(re.findall('[#]', spring_map))
    loc_unknowns = (match.start() for match in re.finditer('[?]', spring_map))
    brute_force = sum(groups) - n_knowns

    part_sum = 0
    for loc in itertools.combinations(loc_unknowns, brute_force):
        
        test_map = [c for c in spring_map]
        for i in loc:
            test_map[int(i)] = '#'
        if checker(''.join(test_map), groups):
            part_sum += 1
    
    return part_sum

part1_sum = 0
for l in L:
    original_map, c = l.split()
    groups = [int(x) for x in c.split(',')]

    spring_map = ''
    for _ in range(4):
        spring_map += '?' + original_map
    
    groups = groups * 5

    part1_sum += get_count(spring_map, len(spring_map), tuple(groups))

def check(map, group, group_location):
    if map[0] == '.':
        check(map[1:], group, group_location)
    
    if map[0] == '?':
        for replace in ['.', '?']:
            map[0] = replace
            check(map[1:], group, group_location)

    



for l in L:

# part2_sum = 0
# for l in L:
#     # l = '?#?#?#?#?#?#?#? 1,3,1,6'
#     # l = '.??..??...?##. 1,1,3'
#     original_map , c = l.split()
#     groups = [int(x) for x in c.split(',')]

#     spring_map = '?' + original_map

#     # Check the original map
#     n_knowns = len(re.findall('[#]', original_map))
#     loc_unknowns = [match.start() for match in re.finditer('[?]', original_map)]
#     brute_force = sum(groups) - n_knowns

#     temp_sum_1 = 0
#     print(loc_unknowns, n_knowns, brute_force)
#     for loc in itertools.combinations(loc_unknowns, brute_force):
#         test_map = [c for c in original_map]
#         for i in loc:
#             test_map[int(i)] = '#'
#         assert ''.join(test_map) != original_map
#         if checker(''.join(test_map), groups):
#             temp_sum_1 += 1

#     n_knowns = len(re.findall('[#]', spring_map))
#     loc_unknowns = [match.start() for match in re.finditer('[?]', spring_map)]
#     brute_force = sum(groups) - n_knowns

#     temp_sum_2 = 0
#     for loc in itertools.combinations(loc_unknowns, brute_force):
#         test_map = [c for c in spring_map]
#         for i in loc:
#             test_map[int(i)] = '#'
#         if checker(''.join(test_map), groups):
#              print(test_map, groups)
#             temp_sum_2 += 1


#     print(temp_sum_1, temp_sum_2)
#     print(temp_sum_1 * temp_sum_2)
    
#     part2_sum += temp_sum_1 * temp_sum_2 
#     print(part2_sum)
#     assert False

print(part1_sum)