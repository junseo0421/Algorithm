import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
cheese_map = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def outside(matrix):
    q = deque()
    q.append((0, 0))

    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    matrix[0][0] = 2

    while q:
        x1, y1 = q.popleft()

        for j in range(4):
            nx1 = x1 + dx[j]
            ny1 = y1 + dy[j]

            if not (0 <= nx1 < N and 0 <= ny1 < M):
                continue

            if visited[nx1][ny1] == 0:
                if matrix[nx1][ny1] == 0:
                    visited[nx1][ny1] = 1
                    matrix[nx1][ny1] = 2  # 바깥 공기를 2로 마킹
                    q.append((nx1, ny1))
                elif matrix[nx1][ny1] == 2:
                    visited[nx1][ny1] = 1
                    q.append((nx1, ny1))

cheeses = []

for i in range(N):
    for j in range(M):
        if cheese_map[i][j] == 1:
            cheeses.append((i, j))

result = 0

while cheeses:
    outside(cheese_map)

    melt = []

    for x, y in cheeses:
        cnt = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < M):
                continue

            if cheese_map[nx][ny] == 2:
                cnt += 1

        if cnt >= 2:
            melt.append((x, y))
            cheese_map[x][y] = 0

    cheeses = [pos for pos in cheeses if pos not in melt]

    result += 1

sys.stdout.write(str(result))