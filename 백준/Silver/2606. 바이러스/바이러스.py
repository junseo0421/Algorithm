import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(K):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

visited = [0] * (N+1)

def dfs(n):
    visited[n] = 1
    for num in graph[n]:
        if visited[num] == 0:
            visited[num] = 1
            dfs(num)

dfs(1)

print(sum(visited) - 1)
