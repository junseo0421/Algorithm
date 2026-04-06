import sys
input = sys.stdin.readline

string = input().rstrip()
result = ''

number0 = number1 = 0

for s in string:
    if s == '1':
        number1 += 1
    else:
        number0 += 1

remove0, remove1 = number0 // 2, number1 // 2

s0 = s1 = 0

for s in string:
    if s == '1':
        if s1 == remove1:
            result += s
        else:
            s1 += 1
    else:
        if s0 != remove0:
            s0 += 1
            result += s

print(result)