import sys

N = int(sys.stdin.readline())

for _ in range(N):
    A, B = sys.stdin.readline().split()
    A = int(A)
    print(''.join(ch*A for ch in B))