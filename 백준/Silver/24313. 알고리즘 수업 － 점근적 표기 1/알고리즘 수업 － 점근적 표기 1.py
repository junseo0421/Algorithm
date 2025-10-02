import sys

a1, a2 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

if (a2 <= (c - a1) * n0) and (a2 <= (c - a1) * 100):
    print(1)
else:
    print(0)