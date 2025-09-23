import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {A} + {B} =", A+B)
