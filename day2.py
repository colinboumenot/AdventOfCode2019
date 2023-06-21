text = list(int(x) for x in open('inputtxt/day2input.txt').read().split(','))


data = [x for x in text]
data[1] = 12
data[2] = 2
current = 0
while True:
    opcode = data[current]
    one, two, three = data[current + 1], data[current + 2], data[current + 3]
    if opcode == 1:
        data[three] = data[one] + data[two]
    elif opcode == 2:
        data[three] = data[one] * data[two]
    else:
        break
    current += 4
print(data[0])

for x in range(100):
    for y in range(100):
        data = [z for z in text]
        data[1] = x
        data[2] = y
        current = 0
        while True:
            opcode = data[current]
            one, two, three = data[current + 1], data[current + 2], data[current + 3]
            if opcode == 1:
                data[three] = data[one] + data[two]
            elif opcode == 2:
                data[three] = data[one] * data[two]
            else:
                break
            current += 4
        if data[0] == 19690720:
            print(x, y)
