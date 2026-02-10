import sys
input = sys.stdin.readline

from collections import deque

delta = ((-1, 0), (0, -1), (0, 1), (1, 0))  # 우선 순위 순서로 설정

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]

baby_shark = ()

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            baby_shark = (i, j)
            space[i][j] = 0


shark_size = 2
eat_cnt = 0

result = 0

while True:
    q = deque()
    q.append(baby_shark)
    visited[baby_shark[0]][baby_shark[1]] = 0

    min_d = 1e6

    eat_lst = []

    while q:
        x, y = q.popleft()

        for dx, dy in delta:
            nx = x + dx
            ny = y + dy

            if not (0 <= nx < N and 0 <= ny < N):
                continue

            if space[nx][ny] > shark_size:
                continue

            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

                if 0 < space[nx][ny] < shark_size:
                    min_d = min(min_d, visited[nx][ny])
                    if visited[nx][ny] == min_d:
                        eat_lst.append((nx, ny))
                        
        if visited[x][y] > min_d:
            break

    # 종료 조건
    if not eat_lst:
        break

    eat_lst = sorted(eat_lst, key=lambda lst:(lst[0], lst[1]))

    result += min_d
    baby_shark = eat_lst[0]
    space[baby_shark[0]][baby_shark[1]] = 0
    visited = [[-1] * N for _ in range(N)]

    eat_cnt += 1

    if eat_cnt == shark_size:
        eat_cnt = 0
        shark_size += 1

sys.stdout.write(str(result))
