text = open('inputtxt/day1input.txt').read().splitlines()

answer = 0

for x in text:
    answer += (int(x) // 3) - 2

print(answer)

answer = 0

for x in text:
    number = int(x)
    while number > 0:
        number = (number // 3) - 2
        if number > 0:
            answer += number

print(answer)