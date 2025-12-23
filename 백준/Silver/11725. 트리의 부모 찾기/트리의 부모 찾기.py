import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n):
    for num in graph[n]:
        if visited[num] == 0:
            visited[num] = n
            dfs(num)

dfs(1)

for i in range(2, N+1):
    sys.stdout.write(str(visited[i]) + '\n')
