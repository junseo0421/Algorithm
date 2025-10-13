import sys

n = int(sys.stdin.readline())

MAX = 10000
count_list = [0] * (MAX+1)

for _ in range(n):
    v = int(sys.stdin.readline())
    count_list[v] += 1

for i in range(MAX+1):
    c = count_list[i]
    if c:
        for _ in range(c):
            print(i)
