import sys

N, K = map(int, sys.stdin.readline().split())

i = 1
num = 0

while True:
    if N % i == 0:
        num += 1

    if num == K:
        break

    if i > N:
        i = 0
        break

    i += 1

print(i)
