import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip())) for _ in range(N)]
depth = [[[-1]*M for _ in range(N)] for _ in range(2)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
q.append((0, 0, 0))  # x, y, crash(0: 아직 안 부숨, 1: 이미 부숨)
depth[0][0][0] = 1

while q:
    x, y, crash = q.popleft()

    if x == N - 1 and y == M - 1:
        sys.stdout.write(str(depth[crash][x][y]))
        exit()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        # 빈 칸으로 이동
        if matrix[nx][ny] == 0 and depth[crash][nx][ny] == -1:
            depth[crash][nx][ny] = depth[crash][x][y] + 1
            q.append((nx, ny, crash))

        # 벽을 아직 안 부쉈고, 이번에 벽을 부수는 경우
        elif matrix[nx][ny] == 1 and crash == 0 and depth[1][nx][ny] == -1:
            depth[1][nx][ny] = depth[crash][x][y] + 1
            q.append((nx, ny, 1))

sys.stdout.write(str(-1))