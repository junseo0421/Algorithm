import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

campus = [input().rstrip() for _ in range(N)]

visited = [[False] * M for _ in range(N)]

pos_i = []

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            pos_i = [i, j]
            break

cnt = 0

def dfs(x, y):
    global cnt

    if x < 0 or x >= N or y < 0 or y >= M:
        return

    if visited[x][y] == True:
        return

    if campus[x][y] == 'X':
        return

    visited[x][y] = True

    if campus[x][y] == 'P':
        cnt += 1

    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

dfs(pos_i[0], pos_i[1])

print(cnt if cnt != 0 else 'TT')
