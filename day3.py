wire_one, wire_two = open('inputtxt/day3input.txt').read().splitlines()
wire_one, wire_two = [line.split(',') for line in [wire_one, wire_two]]

DX = dict(zip('LRUD', [-1, 1, 0, 0]))
DY = dict(zip('LRUD', [0, 0, 1, -1]))

x = 0
x_2 = 0
y = 0
y_2 = 0
wire_length = 0
wire_two_length = 0
points_one = {}
points_two = {}
for command in wire_one:
    direction = command[0]
    move = int(command[1:])
    for _ in range(move):
        x += DX[direction]
        y += DY[direction]
        wire_length += 1
        if (x, y) not in points_one:
            points_one[(x,y)] = wire_length
for command in wire_two:
    direction = command[0]
    move = int(command[1:])
    for _ in range(move):
        x_2 += DX[direction]
        y_2 += DY[direction]
        wire_two_length += 1
        if (x_2, y_2) not in points_two:
            points_two[(x_2, y_2)] = wire_length
intersections = set(points_one.keys()) & set(points_two.keys())
print(min([abs(x) + abs(y) for (x,y) in intersections]))


