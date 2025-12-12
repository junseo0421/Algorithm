import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    if b not in graph[a]:
        graph[a] += [b]
    if a not in graph[b]:
        graph[b] += [a]

# bfs 문제
result = []

def bfs(n):
    visited = [-1] * (N + 1)
    visited[n] = 0

    q = deque([n])

    while q:
        num = q.popleft()

        for i in graph[num]:
            if visited[i] == -1:
                visited[i] = visited[num] + 1
                q.append(i)

    result.append(sum(visited[1:]))


for i in range(1, N+1):
    bfs(i)

print(result.index(min(result)) + 1)
