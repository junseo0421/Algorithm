import sys
input = sys.stdin.readline

N = int(input())
num_lst = [0]

for _ in range(N):
    num_lst.append(int(input()))

ans = []


def dfs(start, now, visit):
    next_node = num_lst[now]

    if visit[next_node] == 0:
        visit[next_node] = 1
        dfs(start, next_node, visit)
    else:
        if next_node == start:
            ans.append(start)


for i in range(1, N + 1):
    visited = [0] * (N + 1)
    visited[i] = 1
    dfs(i, i, visited)

ans.sort()

print(len(ans))
for i in ans:
    print(i)