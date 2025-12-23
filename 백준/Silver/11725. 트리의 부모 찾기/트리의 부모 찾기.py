import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# # dfs
# sys.setrecursionlimit(10**6)
# 
# def dfs(n):
#     for num in graph[n]:
#         if visited[num] == 0:
#             visited[num] = n
#             dfs(num)
# 
# dfs(1)

# bfs
from collections import deque

def bfs(n):
    q = deque([n])

    while q:
        a = q.popleft()

        for num in graph[a]:
            if visited[num] == 0:
                visited[num] = a
                q.append(num)

bfs(1)

for i in range(2, N+1):
    sys.stdout.write(str(visited[i]) + '\n')