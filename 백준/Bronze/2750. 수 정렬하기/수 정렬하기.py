import sys

n = int(sys.stdin.readline())
num_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

for i in sorted(num_list):
    print(i)
