import collections

X_real= [l.strip() for l in open('input.txt')]
X_test = [l.strip() for l in open('input-test-1.txt')]

L = X_real

# Parse to graph form
def get_neighbours(L, current_coordinate):
    neighbours = []
    x, y = current_coordinate
    curr_char = L[y][x]
    
    # '|', y - 1, y + 1
    if curr_char == '|':
        neighbours.append((x, y - 1))
        neighbours.append((x, y + 1))
    # '-', x - 1, x + 1
    elif curr_char == '-':
        neighbours.append((x - 1, y))
        neighbours.append((x + 1, y))
    # 'L', y - 1, x + 1
    elif curr_char == 'L':
        neighbours.append((x, y - 1))
        neighbours.append((x + 1, y))
    # 'J', y - 1, x - 1
    elif curr_char == 'J':
        neighbours.append((x, y - 1))
        neighbours.append((x - 1, y))
    # '7', y + 1, x - 1 
    elif curr_char == '7':
        neighbours.append((x, y + 1))
        neighbours.append((x - 1, y))
    # 'F', y + 1, x + 1
    elif curr_char == 'F':
        neighbours.append((x, y + 1))
        neighbours.append((x + 1, y))
    else:
        print(curr_char)
        assert False, "Not sure why we're here"
    
    return neighbours

def parse_graph(L):
    start = []
    pipe_map = collections.defaultdict(list)
    for y, ly in enumerate(L):
        for x, curr_char in enumerate(ly):
            if curr_char == '.':
                continue
            if curr_char == 'S':
                start = (x, y)
                coordinates = [[0,1],[0,-1],[1,0],[-1,0]]
                for c in coordinates:
                    n = (x + c[0], y + c[1])
                    if L[n[0]][n[1]] != '.':
                        pipe_map[(x,y)].append(n)
                continue 
                
            pipe_map[(x,y)] = get_neighbours(L, (x,y))
    
    return start, pipe_map

def get_cycle(start_coord, pipe_map):
    # temp = []
    stack = set([(start_coord)])
    visited = set([(start_coord)])

    steps = -1
    while stack:
        next = set()
        for curr in stack:
            for edges in pipe_map[curr]:
                if edges not in visited and curr in pipe_map.get(edges, []):
                    next.add(edges)
                    visited.add(curr)
        stack = next
        steps += 1
    
    return steps

   
# Find loops
# print(get_cycle('A', test_map))
start_coord, pipe_map = parse_graph(L)
# print(start_coord, pipe_map)
print(get_cycle(start_coord, pipe_map))
# print(set(visited_list))