import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

map_lst = [[-1 if x == 1 else x for x in map(int, input().split())] for _ in range(N)]

x, y = -1, -1

for i in range(N):
    for j in range(M):
        if map_lst[i][j] == 2:
            x, y = i, j
            break

    if x != -1 and y != -1:
        break

def bfs(a, b):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    q.append([a, b])

    map_lst[a][b] = 0

    while q:
        a, b = q.popleft()

        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if map_lst[nx][ny] == -1:
                map_lst[nx][ny] = map_lst[a][b] + 1
                q.append([nx, ny])

bfs(x, y)

for num_lst in map_lst:
    print(*num_lst)
