import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())

tree = [[] for _ in range(N+1)]


for _ in range(N-1):
    parent, child, weight = map(int, input().split())

    tree[child].append((parent, weight))
    tree[parent].append((child, weight))

def dfs(n):
    for i in tree[n]:
        if visited[i[0]] == -1:
            visited[i[0]] = visited[n] + i[1]
            dfs(i[0])

visited = [-1] * (N+1)
visited[1] = 0
dfs(1)

a = visited.index(max(visited))

visited = [-1] * (N+1)
visited[a] = 0
dfs(a)
sys.stdout.write(str(max(visited)))
