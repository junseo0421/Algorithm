import sys
input = sys.stdin.readline

from collections import deque  # BFS

N = int(input())
K = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(K):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

visited = [0] * (N+1)
visited[1] = 1
Q = deque([1])

while Q:
    c = Q.popleft()
    for num in graph[c]:
        if visited[num] == 0:
            Q.append(num)
            visited[num] = 1

print(sum(visited) - 1)
