import sys

N = int(sys.stdin.readline())

for i in range(N):
    print(sum(list(map(int, sys.stdin.readline().split()))))
