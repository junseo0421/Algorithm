import sys

N = int(sys.stdin.readline())
C = 0

for i in range(N+1):
    if i == 0:
        C = 2
        continue
    C = C * 2 - 1

print(C**2)