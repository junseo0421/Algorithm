import sys

N, M = map(int, sys.stdin.readline().split())

basket = []

for i in range(N):
    basket.append(i+1)

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    basket[A-1], basket[B-1] = basket[B-1], basket[A-1]

for i in basket:
    print(i, end=" ")
