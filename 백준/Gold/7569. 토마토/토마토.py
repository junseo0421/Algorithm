import sys
input = sys.stdin.readline

from collections import deque

M, N, H = map(int, input().split())  # 가로, 세로, 높이
box = []
q = deque()

for h in range(H):
    layer = []
    for n in range(N):
        row = list(map(int, input().split()))
        layer.append(row)
        for m in range(M):
            if row[m] == 1:
                q.append((h, n, m))  # 익은 토마토만 큐에 넣기
    box.append(layer)

# 위, 아래, 앞, 뒤, 왼쪽, 오른쪽
dh = [1, -1, 0, 0, 0, 0]
dn = [0, 0, 1, -1, 0, 0]
dm = [0, 0, 0, 0, 1, -1]

while q:
    h, n, m = q.popleft()

    for i in range(6):
        nh = h + dh[i]
        nn = n + dn[i]
        nm = m + dm[i]

        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
            if box[nh][nn][nm] == 0:
                box[nh][nn][nm] = box[h][n][m] + 1
                q.append((nh, nn, nm))

answer = 0

for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                print(-1)
                exit()
            answer = max(answer, box[h][n][m])

print(answer - 1)