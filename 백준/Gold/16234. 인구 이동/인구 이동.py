# 최적화 버전

import sys
input = sys.stdin.readline

from collections import deque

N, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

if N == 1:
    sys.stdout.write('0')
    exit()

# 인접 좌표 미리 구해두기
neighbor = {
    (x, y): [(x + dx, y + dy) for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)) if (0 <= x + dx < N and 0 <= y + dy < N)]
    for x in range(N)
    for y in range(N)
}

day = 0

# 체크판 식으로 초기 시작점을 절반 정도로 줄임
queue = [(i, j) for i in range(N) for j in range(i%2, N, 2)]

# visited를 day 값으로 관리
visited = [[-1] * N for _ in range(N)]

while True:
    # 마지막에 평균값 넣어줄 때 사용할 dict
    avg_dict = {}

    # 다음 날 탐색 시작점
    next_queue = []

    # 이번 날에 필요한 칸만 순회
    for i, j in queue:
        if visited[i][j] == day:
            continue

        # bfs 적용
        q = deque([(i, j)])
        union = [(i, j)]
        visited[i][j] = day

        summation = maps[i][j]
        cnt = 1

        while q:
            x, y = q.popleft()

            for nx, ny in neighbor[(x, y)]:
                if visited[nx][ny] == day:
                    continue

                # 차이의 절댓값이 L과 R 사이인 칸 큐에 넣기
                if L <= abs(maps[x][y] - maps[nx][ny]) <= R:
                    visited[nx][ny] = day
                    q.append((nx, ny))
                    union.append((nx, ny))
                    summation += maps[nx][ny]
                    cnt += 1

        if cnt == 1:
            continue

        avg = summation // cnt

        for pos in union:
            avg_dict[pos] = avg

        # 연합이 생긴 좌표들만 다음 날 시작점 후보로 넘김
        next_queue.extend(union)

    if not next_queue:
        sys.stdout.write(str(day))
        break

    # 탐색이 '모두' 끝난 후, 미리 저장해둔 좌표에 평균 인구 넣기
    for position, av in avg_dict.items():
        maps[position[0]][position[1]] = av

    queue = next_queue
    day += 1