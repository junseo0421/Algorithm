import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

if A >= V:
    print("1")
elif V-A <= A-B:
    print("2")
else:
    print(1 + math.ceil((V-A)/(A-B)))
