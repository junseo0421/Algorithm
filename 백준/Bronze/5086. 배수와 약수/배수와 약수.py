import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    
    if A == 0 and B == 0:
        break

    if A % B == 0:
        print("multiple")
    elif B % A == 0:
        print("factor")
    else:
        print("neither")
