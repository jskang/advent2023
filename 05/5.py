X_real= [l.strip() for l in open('5-input')]
X_test = [l.strip() for l in open('5-input-test')]

X = X_real

def get_row(X, i):
    row = []
    counter = 1 
    while i + counter < len(X) and X[i + counter]:
        row.append([int(l) for l in X[i + counter].split()])
        counter += 1
    
    return row, counter

full_map = []

counter = 0
for i in range(len(X)):
    if counter:
        counter -= 1
        continue 

    if i == 0:
        seeds = [int(x) for x in X[i].split(':')[1].split()]
    if X[i].startswith('seed-to-soil'):
        row, counter = get_row(X, i)
        full_map.append(row)
    if X[i].startswith('soil-to-fertilizer'):
        row, counter = get_row(X, i)
        full_map.append(row)
    if X[i].startswith('fertilizer-to-water'):
        row, counter = get_row(X, i)
        full_map.append(row)
    if X[i].startswith('water-to-light'):
        row, counter = get_row(X, i)
        full_map.append(row)
    if X[i].startswith('light-to-temperature'):
        row, counter = get_row(X, i)
        full_map.append(row)
    if X[i].startswith('temperature-to-humidity'):
        row, counter = get_row(X, i)
        full_map.append(row)
    if X[i].startswith('humidity-to-location'):
        row, counter = get_row(X, i)
        full_map.append(row)

mininum_location =  9999999999999999

for seed in seeds:
    tracker = seed
    for mapping in full_map:
        for sl in mapping:
            if tracker <= sl[1] + sl[2] - 1 and tracker >= sl[1]:
                tracker = sl[0] + (tracker - sl[1])
                break
        
    mininum_location = min(mininum_location, tracker)
    
print('part1: ', mininum_location)


# reverse and brute force
# time python3 5.py
# real    16m28.879s
# user    16m28.860s
# sys     0m0.000s
found = False
# We know the answer, for demonstration use the higher location
# location = 27992000 
# location = 0
# while found is False:
#     location += 1
#     tracker = location
#     for mapping in reversed(full_map):
#         for sl in mapping:
#             if tracker <= sl[0] + sl[2] - 1 and tracker >= sl[0]:
#                 tracker = sl[1] + (tracker - sl[0])
#                 break
    
#     for i in range(0, len(seeds), 2):
#         lb = seeds[i]
#         ub = seeds[i + 1]
#         if tracker >= lb and tracker < lb + ub:
#             print('part2: ', location)
#             found = True

range_map = [(X[i], X[i+1]) for i in range(0, len(seeds), 2)]
queue = range_map


for mapping in full_map:
    new_range = []
    while len(queue):
        range_start, range_end = queue.pop()
        for dest, source, n in mapping:
            source_start = source
            source_end = source + n
            mapping = dest - source 

            if source_end > range_end and source_start <= range_start: 
                # range:             |<--1-->|
                # source:        |<------------->|
                new_range.append((range_start + mapping, range_end + mapping))
                break
            if range_end > source_end and range_start <= source_start:
                # range:   |<-1->|<------2------>|<-3->|
                # source:        |<------------->|
                # map part 2 to dest by adding the diff between dest and source
                # put part 1, and part 3 into queue
                # calculate the mapping diff
                # part 2
                new_range.append((source_start + mapping, source_end + mapping))
                # part 1
                queue.append((range_start, source_start))
                # part 3
                queue.append((source_end, range_end))
            if range_end > source_end and range_start <= source_start:
                # range:   |<-1->|<-2->|
                # source:        |<------------->|
            if range_end > source_end and range_start <= source_start:
                # range:                   |<-1->|<-2->|
                # source:        |<------------->|           
            if range_end > source_end and range_start <= source_start:
                # range:  |<-1->|         or          |<-1->|              
                # source:          |<------------->|           
# calculate the interval based on mapping
# Find the range that overlaps between range_map, and for the ones that don't create a new range
