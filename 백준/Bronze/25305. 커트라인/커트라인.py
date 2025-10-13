import sys

n, k = map(int, sys.stdin.readline().split())
num_list = sorted(list(map(int, sys.stdin.readline().split())))

print(num_list[n-k])
