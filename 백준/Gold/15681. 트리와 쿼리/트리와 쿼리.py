import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N, R, Q = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

for _ in range(N-1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

def dfs(start):
    visited[start] = 1

    for child in graph[start]:
        if visited[child] == -1:  # 양방향 고려
            dfs(child)
            visited[start] += visited[child]

dfs(R)

for _ in range(Q):
    q = int(input())
    sys.stdout.write(str(visited[q]) + "\n")