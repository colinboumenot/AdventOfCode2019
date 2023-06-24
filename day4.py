text = open('inputtxt/day4input.txt').read().split('-')
from collections import Counter
answer = 0

for x in range(int(text[0]), int(text[1]) + 1):
    if list(str(x)) == sorted(str(x)):
        if any(y >= 2 for y in Counter(str(x)).values()):
            answer += 1
print(answer)

answer = 0

for x in range(int(text[0]), int(text[1]) + 1):
    if list(str(x)) == sorted(str(x)):
        if any(y == 2 for y in Counter(str(x)).values()):
            answer += 1
print(answer)
