
def run(line):
    values = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]
    data = [int(x) for x in line] + ([0] * 10000)
    input_id = 0
    relative_base = 0

    while data[input_id] != 99:
        sets = [int(x) for x in f'{data[input_id]:0>5}'[:3]][::-1]
        opcode = int(f'{data[input_id]:0>5}'[3:])
        temp_base = [relative_base if sets[x] == 2 else 0 for x in range(values[opcode])]
        value = [data[input_id + x + 1] if sets[x] == 1 else data[temp_base[x] + data[input_id + x + 1]] for x in range(values[opcode])]
        if opcode == 1:
            data[temp_base[2] + data[input_id + 3]] = value[0] + value[1]
        elif opcode == 2:
            data[data[input_id + 3] + temp_base[2]] = value[0] * value[1]
        elif opcode == 3:
            data[data[input_id + 1] + temp_base[0]] = int(input('input: '))
        elif opcode == 4:
            print(value[0])
        elif opcode == 5:
            if value[0] != 0:
                input_id = value[1] - 3
        elif opcode == 6:
            if value[0] == 0:
                input_id = value[1] - 3
        elif opcode == 7:
            data[data[input_id + 3] + temp_base[2]] = int(value[0] < value[1])
        elif opcode == 8:
            data[data[input_id + 3] + temp_base[2]] = int(value[0] == value[1])
        elif opcode == 9:
            relative_base += value[0]
        input_id += values[opcode] + 1
    return data

text = open('inputtxt/day9input.txt').readline().split(',')
print(run(text))