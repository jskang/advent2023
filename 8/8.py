import collections
from math import gcd
import re
X_real= [l.strip() for l in open('8-input')]
X_test = [l.strip() for l in open('8-input-test')]

X = X_real
instruction = X[0]
nodes = X[2:]

def produce_mapping(nodes, re_start, re_nodes):
    mapping = {}
    start_nodes = []
    for n in nodes:
        curr, left, right = re.findall(re_nodes, n)
        mapping[curr] = [left, right]
        if re.search(re_start, curr):
            start_nodes.append(curr)
    
    return mapping, start_nodes

def count_to_end(mapping, start_node_list, end_regex):
    answer = []
    start_nodes = [mapping[n] for n in start_node_list ]
    for node in start_nodes:
        count = 0
        cn = node
        nn = ''
        while True:
            if re.search(end_regex, nn):
                break
            for i in instruction:
                count += 1
                index = 0 if i == "L" else 1
                nn = cn[index]
                cn = mapping[nn]

        answer.append(count)
    return answer

part1_mapping, part1_start_list = produce_mapping(nodes, 'AAA', '[A-Z]+')
part2_mapping, part2_start_list = produce_mapping(nodes, '[0-9A-Z]{2}A', '[0-9A-Z]+')

parts_arg = [
    (part1_mapping, part1_start_list, 'ZZZ'),
    (part2_mapping, part2_start_list, '[0-9A-Z]{2}Z')
]

parts_answer = []
for mapping, start_nodes_list, end_regex in parts_arg:
    parts_answer.append(count_to_end(mapping, start_nodes_list, end_regex))

print('part1: ', parts_answer[0][0])

# calculate least common multiple
lcm = 1
for i in parts_answer[1]:
    lcm = lcm * i // gcd(lcm, i)

print('part2: ', lcm)