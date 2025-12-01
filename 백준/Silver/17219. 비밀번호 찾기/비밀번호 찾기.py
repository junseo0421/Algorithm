import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dict = {}

for _ in range(N):
    ad, pw = input().split()
    dict[ad] = pw
    
for _ in range(M):
    print(dict[input().rstrip()])
    