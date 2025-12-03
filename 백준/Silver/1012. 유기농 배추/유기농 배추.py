import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        pos_x, pos_y = q.popleft()

        for i in range(4):
            nx = pos_x + dx[i]
            ny = pos_y + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue

            if table[nx][ny] == 1:
                q.append((nx, ny))
                table[nx][ny] = 0


for _ in range(T):
    M, N, K = map(int, input().split())  # 가로 길이(열), 세로 길이 (행)

    table = [[0] * N for _ in range(M)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        table[x][y] = 1

    for a in range(M):
        for b in range(N):
            if table[a][b] == 1:
                bfs(a, b)
                cnt += 1

    print(cnt)
