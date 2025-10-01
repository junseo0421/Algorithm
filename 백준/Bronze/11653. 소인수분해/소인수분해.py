import sys

N = int(sys.stdin.readline())

while True:
    if N == 1:
        break

    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            N = N // i
            print(i)
            break
    else:
        print(N)
        break
