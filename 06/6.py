import math
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
results = 0
for acc_time in range(allowed_time):
    coast_time = j_time - acc_time
    coast_distance = coast_time * acc_time

    if coast_distance > j_distance:
        results = acc_time
        break
# since the solution is mirrored, you only have to do one side
print('part2: ', (allowed_time - 2 * results))

# quadratic_formula way
# acc_time = x
# 
# j_distance = (j_time - acc_time) * acc_time
# j_distance = -acc_time^2 + j_time * acc_time
# 0 = acc_time ^2 - j_time * acc_time + j_distance
# 0 = 1(x^2) - j_time(x) +j_distance 
# (-(-j_time) +/- sqrt((j_time)^2 - 4 * 1 * j_distance)) / 2 * 1
# (j_time +/- sqrt(j_time**2 - 4*j_distance)) /2
# root1 = math.floor((j_time + math.sqrt(pow(j_time, 2) - 4 * j_distance))) // 2
# root2 = math.ceil((j_time - math.sqrt(pow(j_time, 2) - 4 * j_distance))) // 2
# difference between root1 and root2

print('part2 quadratic formula: ', int(math.sqrt(pow(j_time, 2) - 4 * j_distance)))