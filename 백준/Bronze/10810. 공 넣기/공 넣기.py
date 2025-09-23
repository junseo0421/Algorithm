import sys

N, M = map(int, sys.stdin.readline().split())

basket = [0]*N

for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    
    for i in range(A-1, B):
        basket[i] = C
        
for i in basket:
    print(i, end=" ")
    