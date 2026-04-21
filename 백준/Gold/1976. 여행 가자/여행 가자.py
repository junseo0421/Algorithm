import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for i in range(N):
    adj_lst = list(map(int, input().split()))

    for j in range(N):
        if adj_lst[j] == 1:
            graph[i+1].append(j+1)

plan = list(map(int, input().split()))
visited = [0] * (N + 1)

q = deque()
q.append(plan[0])
visited[plan[0]] = 1

while q:
    a = q.popleft()

    for nxt in graph[a]:
        if visited[nxt] == 0:
            visited[nxt] = 1
            q.append(nxt)

for p in plan:
    if visited[p] == 0:
        print('NO')
        break
else:
    print('YES')