import sys
input = sys.stdin.readline

from collections import deque

N, d, k, c = map(int, input().split())

sushi = []
result_lst = [[] for _ in range(k+1)]

for _ in range(N):
    ss = int(input())
    sushi.append(ss)

right = N-1
left = right - k + 1

s = deque()

ans = 0

for i in range(left, right + 1):
    s.append(sushi[i])

    length = len(set(s))

    if c in list(s):
        ans = max(ans, length + 1)
    else:
        ans = max(ans, length)

while 0 <= right:
    left -= 1
    right -= 1

    s.pop()
    s.appendleft(sushi[left])

    length = len(set(s))

    if length < ans:
        continue

    if c in s:
        ans = max(ans, length)
    else:
        ans = max(ans, length + 1)

print(ans)