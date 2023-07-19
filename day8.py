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

print(answer)
