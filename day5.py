text = [int(x) for x in open('inputtxt/day5input.txt').read().split(',')]
from copy import deepcopy
text_one = deepcopy(text)
text_two = deepcopy(text)

def cleanup(command):
    command = f"{command:05}"
    return command[3:], command[0:3]

def get_value(command, point, opcode, sets):
    set_a, set_b, set_c = sets
    return_value = []
    if opcode in ['01', '02', '04']:
        if set_c == '0':
            return_value.append(command[command[point + 1]])
        else:
            return_value.append(command[point + 1])
        if opcode in ['01', '02']:
            if set_b == '0':
                return_value.append(command[command[point + 2]])
            else:
                return_value.append(command[point + 2])
            if opcode in []:
                if set_a == '0':
                    return_value.append(command[command[point + 3]])
                else:
                    return_value.append(command[point + 3])
    return return_value

index = 0
input = 1

while text_one[index] != 99:
    opcode, sets = cleanup(text_one[index])
    value = get_value(text_one, index, opcode, sets)
    if opcode == '01':
        text_one[text_one[index + 3]] = value[0] + value[1]
        index += 4
    if opcode == '02':
        text_one[text_one[index + 3]] = value[0] * value[1]
        index += 4
    if opcode == '03':
        text_one[text_one[index + 1]] = input
        index += 2
    if opcode == '04':
        print(value[0])
        index += 2
