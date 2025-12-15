import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

graph = [[] for _ in range(N)]

for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if lst[j] == 1:
            graph[i] += [j]

def bfs(n):
    visited = [0] * N

    q = deque([n])

    while q:
        num = q.popleft()

        for g in graph[num]:
            if visited[g] == 0:
                visited[g] = 1
                q.append(g)

    print(*visited)

for i in range(N):
    bfs(i)
