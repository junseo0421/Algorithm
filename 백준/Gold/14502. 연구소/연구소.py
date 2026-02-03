import sys
input = sys.stdin.readline

from itertools import combinations
from collections import deque

N, M = map(int, input().split())
map_lst = [list(map(int, input().split())) for _ in range(N)]

empties = []
viruses = []

for i in range(N):
    for j in range(M):
        if map_lst[i][j] == 0:
            empties.append((i, j))
        elif map_lst[i][j] == 2:
            viruses.append((i, j))

max_result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for (a, b, c) in combinations(empties, 3):
    result = 0
    new_map = [row[:] for row in map_lst]

    new_map[a[0]][a[1]] = 1
    new_map[b[0]][b[1]] = 1
    new_map[c[0]][c[1]] = 1

    q = deque()

    for virus in viruses:
        q.append(virus)

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < M):
                continue

            if new_map[nx][ny] == 0:
                new_map[nx][ny] = 2
                q.append((nx, ny))

    for i in range(N):
        for j in range(M):
            if new_map[i][j] == 0:
                result += 1

    max_result = max(max_result, result)

sys.stdout.write(str(max_result))