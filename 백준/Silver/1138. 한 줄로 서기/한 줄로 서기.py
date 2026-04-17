import sys
input = sys.stdin.readline

# 키가 큰 사람이 왼쪽에 몇 명이 있었는지

N = int(input())
num_lst = list(map(int, input().split()))

ans = []

for i in range(N-1, -1, -1):
    ans.insert(num_lst[i], i+1)

print(' '.join(map(str, ans)))
