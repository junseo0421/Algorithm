import sys
input = sys.stdin.readline

from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

# dfs
def dfs(v):
    if visited[v] == 0:
        visited[v] = 1
        visited_lst.append(v)

    for i in sorted(graph[v]):
        if visited[i] == 0:
            visited_lst.append(i)
            visited[i] = 1
            dfs(i)

# bfs
def bfs(v):
    q = deque()
    q.append(v)

    while q:
        num = q.popleft()
        if visited[num] == 0:
            visited_lst.append(num)
            visited[num] = 1

        for i in sorted(graph[num]):
            if visited[i] == 0:
                q.append(i)
                visited_lst.append(i)
                visited[i] = 1

visited_lst = []
visited = [0] * (N+1)
dfs(V)
sys.stdout.write(' '.join(map(str, visited_lst))+'\n')

visited_lst = []
visited = [0] * (N+1)
bfs(V)
sys.stdout.write(' '.join(map(str, visited_lst)))