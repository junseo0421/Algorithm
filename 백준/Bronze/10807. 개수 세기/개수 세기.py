import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
n_find = int(sys.stdin.readline())

print(num_list.count(n_find))
