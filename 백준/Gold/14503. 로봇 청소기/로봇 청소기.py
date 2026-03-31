import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
clean = [[0] * M for _ in range(N)]

# dn = ((1, 0), (0, -1), (-1, 0), (0, 1))  # 남, 서, 북, 동 방향
# dn = ((0, -1), (1, 0), (0, 1), (-1, 0))   # 서, 남, 북, 동 방향
dn = ((-1, 0), (0, 1), (1, 0), (0, -1)) # 북, 동, 남, 서

# d = 0 > 3, 2, 1, 0
# d = 1 > 0, 3, 2, 1
# d = 2 > 1, 0, 3, 2
# d = 3 > 2, 1, 0, 3

q = [(r, c, d)]

while q:
    r, c, d = q.pop()
    clean[r][c] = 1

    for i in range(4):  # 방향을 기준으로 어디부터 보냐를 결정해야함
        dr, dc = dn[(d + 3 - i) % 4]

        nr = r + dr
        nc = c + dc

        if room[nr][nc] == 0 and clean[nr][nc] == 0:
            q.append((nr, nc, (d + 3 - i) % 4))
            break

    if not q:
        dr, dc = dn[(d+2) % 4]
        if room[r + dr][c + dc] == 0:
            q.append((r + dr, c + dc, d))

sys.stdout.write(str(sum(map(sum, clean))))
