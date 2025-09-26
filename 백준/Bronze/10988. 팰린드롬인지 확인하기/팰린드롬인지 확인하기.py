import sys

A = sys.stdin.readline().rstrip()

x = len(A)//2

if len(A) % 2 == 0:
    left = A[:x]
    right = A[x:]
else:
    left = A[:x]
    right = A[x + 1:]

print("1" if left == right[::-1] else "0")
