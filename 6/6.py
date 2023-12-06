import collections
X_real= [l.strip() for l in open('6-input')]
X_test = [l.strip() for l in open('6-input-test')]

X = X_real

times = [int(x) for x in X[0].split(':')[1].split()]
distances = [int(x) for x in X[1].split(':')[1].split()]

j_time = int(''.join([str(t) for t in times]))
j_distance = int(''.join([str(t) for t in distances]))

# part 1
sum_total = 1
for i in range(len(times)):
    count = 0
    allowed_time = times[i] + 1

    for acc_time in range(allowed_time):
        coast_time = times[i] - acc_time
        coast_distance = coast_time * acc_time

        if coast_distance > distances[i]:
            count += 1
    sum_total *= count
print('part1: ', sum_total)

# part 2
allowed_time = j_time + 1
results = []
for search_order in [range(allowed_time), reversed(range(allowed_time))]:
    for acc_time in search_order:
        coast_time = j_time - acc_time
        coast_distance = coast_time * acc_time

        if coast_distance > j_distance:
            results.append(acc_time)
            break
    
# Do a +1 to include the lowest number in the interval since we are subtracting
print('part2: ', results[1] - results[0] + 1)