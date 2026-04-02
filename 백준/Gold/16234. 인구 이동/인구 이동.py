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

result = 0

while True:
    # visited 2차원 배열은 while 문 안에 있어야함
    visited = [[0] * N for _ in range(N)]

    # 마지막에 평균값 넣어줄 때 사용할 list
    avg_dict = {}

    # 모든 칸 순회
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                continue

            # bfs 적용
            q = deque([(i, j)])
            summation = 0
            cnt = 0
            union = []

            while q:
                x, y = q.popleft()

                if visited[x][y] == 1:
                    continue

                # 큐에 넣으면서 같은 연합인 부분의 좌표는 미리 다 저장해두기 (합도 미리 저장)
                union.append((x, y))

                visited[x][y] = 1
                summation += maps[x][y]
                cnt += 1

                for nx, ny in neighbor[(x, y)]:
                    if visited[nx][ny] == 1:
                        continue

                    # 차이의 절댓값이 L과 R 사이인 칸 큐에 넣기
                    if L <= abs(maps[x][y] - maps[nx][ny]) <= R:
                        q.append((nx, ny))

            if cnt == 1:
                continue

            avg = summation // cnt

            for pos in union:
                avg_dict[pos] = avg

    if not avg_dict:
        sys.stdout.write(str(result))
        break

    # 탐색이 '모두' 끝난 후, 미리 저장해둔 좌표에 평균 인구 넣기
    for position, av in avg_dict.items():
        maps[position[0]][position[1]] = av

    result += 1