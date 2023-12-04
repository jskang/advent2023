# didn't clean up or refactor, not sure if it works, also it's not the best implementation closer to garbage and lucky that it worked
X = [l.strip() for l in open('1-input-test')]

numbers = {'one': '1', 'two': '2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

# preprocessing

new_x_forward = []
new_x_backward = []

for x in X:
    new_string = x
    for i in range(len(x)):
        for key, value in numbers.items():
            if new_string[i:].find(key) == 0:
                new_new_string = new_string[i:].replace(key, value)
                new_string = new_string[:i] + new_new_string
    new_x_forward.append(new_string)

for x in X:
    new_string = x
    for i in reversed(range(len(x))):
        for key, value in numbers.items():
            if new_string[i:].find(key) == 0:
                new_new_string = new_string[i:].replace(key, value)
                new_string = new_string[:i] + new_new_string
    new_x_backward.append(new_string)

sum = 0
for i in range(len(new_x_forward)):
    xf = new_x_forward[i]
    xb = new_x_backward[i]

    for c in xf:
        if c.isdigit():
            first_digit = c
            break

    for c in reversed(xb):
        if c.isdigit():
            last_digit = c 
            break

    output = first_digit + last_digit
    sum += int(output)
    print(X[i], xf, output, sum)


print(sum)