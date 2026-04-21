import sys
input = sys.stdin.readline

from collections import deque

# 불 먼저 탐색 후 불이 도달하는 시간 기록
# 그 뒤에 지훈이 bfs 구함

R, C = map(int, input().split())
map_lst = [input().rstrip() for _ in range(R)]
depth = [[[-1] * C for _ in range(R+1)] for _ in range(2)]  # fire(0: fire, 1: ji), x, y

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

ji = (-1, -1)
fire = []

for i in range(R):
    for j in range(C):
        if map_lst[i][j] == 'J':
            ji = (i, j)
            depth[1][i][j] = 0
        elif map_lst[i][j] == 'F':
            fire.append((i, j))
            depth[0][i][j] = 0

q = deque()

for f in fire:
    q.append(f)

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < R and 0 <= ny < C):
            continue

        if map_lst[nx][ny] != '#' and depth[0][nx][ny] == -1:
            depth[0][nx][ny] = depth[0][x][y] + 1
            q.append((nx, ny))

q = deque()

q.append(ji)

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < R and 0 <= ny < C):
            print(depth[1][x][y] + 1)
            exit()

        if map_lst[nx][ny] != '#' and depth[1][nx][ny] == -1:
            if depth[0][nx][ny] == -1 or depth[1][x][y] + 1 < depth[0][nx][ny]:
                depth[1][nx][ny] = depth[1][x][y] + 1
                q.append((nx, ny))

print('IMPOSSIBLE')