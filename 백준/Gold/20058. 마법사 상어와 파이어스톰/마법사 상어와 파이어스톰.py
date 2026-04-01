import sys
input = sys.stdin.readline

from collections import deque

N, Q = map(int, input().split())
S = 2 ** N
ices = [list(map(int, input().split())) for _ in range(S)]
L = list(map(int, input().split()))

# 격자 기준으로 시계방향 90도
# 이후 인접 칸에서 얼음이 0, 1, 2 개 있으면 양 1 줄어듦

# 가장 큰 덩어리는 bfs or dfs로 찾기. visited 로 관리.

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

for l in L:
    if l == 0:
        new_ices = ices
    else:
        new_ices = [[0] * S for _ in range(S)]
        size = 2 ** l  # 격자 size

        for sr in range(0, S, size):
            for sc in range(0, S, size):  # (sr, sc) 가 각 격자의 시작점
                for i in range(size):
                    for j in range(size):  # 내부 사각형 순회
                        new_ices[sr + j][sc + (size - 1 - i)] = ices[sr + i][sc + j]

    # 돌린 이후 얼음 녹이기
    melt = []

    for i in range(S):
        for j in range(S):
            if new_ices[i][j] <= 0:
                continue

            adj_num = 0

            for z in range(4):
                ni = i + dr[z]
                nj = j + dc[z]

                if not (0 <= ni < S and 0 <= nj < S):
                    continue

                if new_ices[ni][nj] > 0:
                    adj_num += 1

            if adj_num < 3:
                melt.append((i, j))

    for x, y in melt:
        new_ices[x][y] -= 1

    ices = new_ices

sys.stdout.write(str(sum(map(sum, ices))) + '\n')

visited = [[0] * S for _ in range(S)]

is_ices = []

for i in range(S):
    for j in range(S):
        if ices[i][j] != 0:
            is_ices.append((i, j))

if len(is_ices) == S ** 2:
    sys.stdout.write(str(S ** 2))
    exit()

max_ices = 0

for x, y in is_ices:
    if visited[x][y] == 1:
        continue

    q = deque()
    q.append((x, y))
    result = 0

    while q:
        r, c = q.popleft()

        if visited[r][c] == 1:
            continue

        result += 1

        visited[r][c] = 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if not (0 <= nr < S and 0 <= nc < S):
                continue

            if visited[nr][nc] == 1:
                continue

            if ices[nr][nc] != 0:
                q.append((nr, nc))


    if result >= (S ** 2 // 2):
        sys.stdout.write(str(result))
        exit()

    max_ices = max(max_ices, result)

sys.stdout.write(str(max_ices))