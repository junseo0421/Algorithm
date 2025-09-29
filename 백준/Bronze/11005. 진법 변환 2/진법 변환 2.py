import sys

N, B = map(int, sys.stdin.readline().split())

total = []

while N >= B:
    N, re = N // B, N % B
    total.append(re)

total.append(N)

print(''.join([str(i) if i<10 else chr(i+55) for i in total])[::-1])
