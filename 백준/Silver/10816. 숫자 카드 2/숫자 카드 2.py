import sys

n = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))
dict = {}

for i in card_list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

m = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split()))

result = []
for check in check_list:
    if check in dict:
        result.append(dict[check])
    else:
        result.append(0)

sys.stdout.write(' '.join(map(str, result)))
