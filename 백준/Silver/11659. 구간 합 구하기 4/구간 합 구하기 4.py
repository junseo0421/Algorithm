import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    lst[i] += lst[i-1]
    
for _ in range(M):
    start, end = map(int, input().split())
    print(lst[end] - lst[start-1])
    