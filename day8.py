text = open('inputtxt/day8input.txt').read()
from math import inf
picture = list(text)
picture_grid = picture[:25 * 6]
low = inf
answer = 0

while picture:
    layer = picture[:25 * 6]
    picture = picture[25 * 6:]
    zeroes = layer.count('0')
    if zeroes < low:
        low = zeroes
        answer = layer.count('1') * layer.count('2')
    string = ''
    for number_one, number_two in zip(layer, picture_grid):
        if number_two == '2':
            string += number_one
        else:
            string += number_two
    picture_grid = string
print(answer)
for x in range(6):
    print(picture_grid[x * 25: (x + 1) * 25].replace('0', ' '))
