import sys
input = sys.stdin.readline

string = input().rstrip()

a_total = 0

for s in string:
    if s == 'a':
        a_total += 1

window = string[:a_total]

a_num = 0

for w in window:
    if w == 'a':
        a_num += 1

com_string = string + string

ans = a_num

for i in range(len(string)):
    if com_string[i] == 'a':
        a_num -= 1

    if com_string[i+a_total] == 'a':
        a_num += 1

    ans = max(a_num, ans)

print(a_total - ans)