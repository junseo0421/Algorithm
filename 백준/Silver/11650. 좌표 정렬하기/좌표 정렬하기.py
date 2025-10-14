import sys

n = int(sys.stdin.readline())
num_list = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    num_list.append([a, b])

for i in sorted(num_list, key=lambda x: (x[0], x[1])):
    print(*i)
