import sys
sys.setrecursionlimit(10**6)   # 🔹 재귀 한도 늘리기
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(n):
    visited[n] = 1
    for num in graph[n]:
        if visited[num] == 0:
            dfs(num)

cnt = 0

for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

sys.stdout.write(str(cnt))
