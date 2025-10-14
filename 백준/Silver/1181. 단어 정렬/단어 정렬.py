import sys

n = int(sys.stdin.readline())
alpha_list = []

for _ in range(n):
    alpha_list.append(sys.stdin.readline().rstrip())

for i in sorted(set(alpha_list), key=lambda x: (len(x), x)):
    print(i)
