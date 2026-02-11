import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

V = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(V):
    lst = list(map(int, input().split()))
    n = lst[0]

    length = (len(lst) - 2) // 2

    for i in range(1, length+1):
        graph[n].append((lst[2*i - 1], lst[2*i]))  # (node, cost)

def dfs(start):
    for node, cost in graph[start]:
        if visited[node] == -1:
            visited[node] = visited[start] + cost
            dfs(node)


visited = [-1] * (V+1)
visited[1] = 0
dfs(1)

a = visited.index(max(visited))

visited = [-1] * (V+1)
visited[a] = 0
dfs(a)

sys.stdout.write(str(max(visited)))