import sys

n = int(sys.stdin.readline())
alpha_list = []

for _ in range(n):
    a, b = sys.stdin.readline().split()
    alpha_list.append((int(a), b))

for i in sorted(alpha_list, key=lambda x: x[0]):
    print(*i)
