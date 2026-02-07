import sys
input = sys.stdin.readline

from collections import deque

INF = 1e9

N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip())) for _ in range(N)]
depth = [[[-1]*M for _ in range(N)] for _ in range(2)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
q.append((0, 0, 0))
depth[0][0][0] = 1
depth[1][0][0] = 1

while q:
    x, y, crash = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if depth[crash][nx][ny] != -1:
            continue

        if matrix[nx][ny] == 0:
            depth[crash][nx][ny] = depth[crash][x][y] + 1
            q.append((nx, ny, crash))
        elif matrix[nx][ny] == 1 and crash == 0:
            depth[1][nx][ny] = depth[crash][x][y] + 1
            q.append((nx, ny, 1))

if depth[0][N-1][M-1] == -1 and depth[1][N-1][M-1] == -1:
    sys.stdout.write(str(-1))
elif depth[0][N-1][M-1] == -1:
    sys.stdout.write(str(depth[1][N-1][M-1]))
elif depth[1][N-1][M-1] == -1:
    sys.stdout.write(str(depth[0][N-1][M-1]))
else:
    sys.stdout.write(str(min(depth[0][N-1][M-1], depth[1][N-1][M-1])))