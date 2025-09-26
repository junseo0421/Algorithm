import sys

A = int(sys.stdin.readline())

for i in range(1, A+1):
    print(" " * (A - i) + "*" * (2*i - 1))

for i in range(1, A):
    print(" "*i + "*"*((A-i) * 2 - 1))
