import sys

N = int(sys.stdin.readline())
num_list = map(int, sys.stdin.readline().split())

for i in num_list:
    if i == 1:
        N -= 1
        continue
    elif i == 2:
        continue

    for j in range(2, i//2 + 1):
        if i % j == 0:
            N -= 1
            break

print(N)

