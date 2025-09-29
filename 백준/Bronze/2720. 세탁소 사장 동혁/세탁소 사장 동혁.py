import sys

charge_list = [25, 10, 5]

N = int(sys.stdin.readline())

for i in range(N):
    C = int(sys.stdin.readline())
    total_list = []
    for j in charge_list:
        C, re = C - (C // j * j), C // j
        total_list.append(re)
    total_list.append(C)
    print(*total_list)
