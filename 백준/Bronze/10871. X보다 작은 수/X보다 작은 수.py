import sys

N, X = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

for i in num_list:
    if i < X:
        print(i, end=" ")
