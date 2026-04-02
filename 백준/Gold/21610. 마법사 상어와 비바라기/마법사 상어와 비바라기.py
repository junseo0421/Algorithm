import sys
input = sys.stdin.readline

N, M = map(int, input().split())
baskets = [list(map(int, input().split())) for _ in range(N)]
command = [list(map(int, input().split())) for _ in range(M)]

dx = (1, 1, -1, -1)
dy = (1, -1, 1, -1)


def cloud_move(x, y, d, s):
    x_minus = (x - s) % N
    y_minus = (y - s) % N
    x_plus = (x + s) % N
    y_plus = (y + s) % N

    if d == 1:
        return x, y_minus
    elif d == 2:
        return x_minus, y_minus
    elif d == 3:
        return x_minus, y
    elif d == 4:
        return x_minus, y_plus
    elif d == 5:
        return x, y_plus
    elif d == 6:
        return x_plus, y_plus
    elif d == 7:
        return x_plus, y
    else:
        return x_plus, y_minus


clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for d, s in command:
    new_clouds = []

    for i in range(len(clouds)):
        cx, cy = clouds[i]
        clouds[i] = cloud_move(cx, cy, d, s)

    for x, y in clouds:  # 구름에서 비 내리기
        baskets[x][y] += 1

    for x, y in clouds:  # 대각선 확인 후 물 양 증가
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < N):
                continue

            if baskets[nx][ny] > 0:
                baskets[x][y] += 1

    for i in range(N):
        for j in range(N):
            if (i, j) in clouds:  # 이전 구름 위치 제외
                continue

            if baskets[i][j] >= 2:
                new_clouds.append((i, j))
                baskets[i][j] -= 2

    clouds = new_clouds

sys.stdout.write(str(sum(map(sum, baskets))))