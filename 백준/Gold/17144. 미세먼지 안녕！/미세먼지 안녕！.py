import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(R)]
air = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(R):
    if room[i][0] == -1:
        air.append(i)

for _ in range(T):
    dif_map = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if room[i][j] != -1 and room[i][j] != 0:
                cnt = 0

                for dir in range(4):
                    nx = i + dx[dir]
                    ny = j + dy[dir]

                    if not (0 <= nx < R and 0 <= ny < C):
                        continue

                    if (nx, ny) in {(air[0], 0), (air[1], 0)}:
                        continue

                    cnt += 1
                    dif_map[nx][ny] += room[i][j] // 5

                room[i][j] -= room[i][j] // 5 * cnt

    for i in range(R):
        for j in range(C):
            room[i][j] += dif_map[i][j]

    prev = 0

    for i in range(1, C):
        room[air[0]][i], prev = prev, room[air[0]][i]

    for i in range(air[0]-1, -1, -1):
        room[i][C-1], prev = prev, room[i][C-1]

    for i in range(C-2, -1, -1):
        room[0][i], prev = prev, room[0][i]

    for i in range(1, air[0]):
        room[i][0], prev = prev, room[i][0]

    prev = 0

    for i in range(1, C):
        room[air[1]][i], prev = prev, room[air[1]][i]

    for i in range(air[1] + 1, R):
        room[i][C - 1], prev = prev, room[i][C - 1]

    for i in range(C - 2, -1, -1):
        room[R-1][i], prev = prev, room[R-1][i]

    for i in range(R-2, air[1], -1):
        room[i][0], prev = prev, room[i][0]

result = 0

for i in range(R):
    for j in range(C):
        result += room[i][j]

sys.stdout.write(str(result + 2))