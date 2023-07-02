text_two = open('inputtxt/day7input.txt').read().split(",")


def run(line, input, index):
    values = [0, 3, 3, 1, 1, 2, 2, 3, 3]
    input_id = 0
    while line[index] != 99:
        sets = [int(x) for x in f'{line[index]:0>5}'[:3]][::-1]
        opcode = int(f'{line[index]:0>5}'[3:])
        value = [line[index + x + 1] if sets[x] else line[line[index + x + 1]] for x in range(values[opcode])]
        if opcode == 1:
            line[line[index + 3]] = value[0] + value[1]
        elif opcode == 2:
            line[line[index + 3]] = value[0] * value[1]
        elif opcode == 3:
            line[line[index + 1]] = input[input_id]
            input_id += 1
        elif opcode == 4:
            return (value[0], index + 2)
        elif opcode == 5:
            if value[0] != 0:
                index = value[1] - 3
        elif opcode == 6:
            if value[0] == 0:
                index = value[1] - 3
        elif opcode == 7:
            line[line[index + 3]] = int(value[0] < value[1])
        elif opcode == 8:
            line[line[index + 3]] = int(value[0] == value[1])
        index += values[opcode] + 1
    return [False, False]


def sequence(line, setting, return_value):
    previous = 0
    text = [int(x) for x in line]
    amplifiers = [[text.copy(), 0] for _ in range(5)]
    for x in range(5):
        output, value = run(amplifiers[x][0], [setting[x], previous], amplifiers[x][1])
        previous = output
        amplifiers[x][1] = value
    if not return_value:
        return previous
    index = 0
    while True:
        output, value = run(amplifiers[index][0], [previous], amplifiers[index][1])
        if not output:
            break
        previous = output
        amplifiers[index][1] = value
        index = (index + 1) % 5
    return previous


def permute(array, temp, result, index):
    if index >= len(temp):
        return result.append(temp.copy())
    for x in range(len(array)):
        temp[index] = array[x]
        permute(array[:x] + array[x + 1:], temp, result, index + 1)

result_one = []
result_two = []
permute(list(range(5)), list(range(5)), result_one, 0)
print(max(sequence(text_two, permutation, False) for permutation in result_one))
permute(list(range(5,10)), list(range(5,10)), result_two, 0)
print(max(sequence(text_two, permutation, True) for permutation in result_two))