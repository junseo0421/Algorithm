import sys
input = sys.stdin.readline

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

cctv_lst = []

for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctv_lst.append((office[i][j], i, j))

# 0:상, 1:우, 2:하, 3:좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 각 cctv별 방향 조합
direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

ans = float('inf')

def dfs(idx, board):
    global ans

    # 모든 cctv 탐색 완료 시
    if idx == len(cctv_lst):
        cnt = 0

        for a in range(N):
            for b in range(M):
                if board[a][b] == 0:
                    cnt += 1

        ans = min(ans, cnt)
        return

    cctv_type, x, y = cctv_lst[idx]

    # 각 cctv 타입 별 방향 조합 중 하나
    for dirs in direction[cctv_type]:
        # board deepcopy
        new_board = [row[:] for row in board]

        # 한 cctv가 여러 방향을 보는 경우 고려
        for d in dirs:
            nx = x + dx[d]
            ny = y + dy[d]

            while 0 <= nx < N and 0 <= ny < M:
                # 벽을 만나면 break
                if new_board[nx][ny] == 6:
                    break

                if new_board[nx][ny] == 0:
                    new_board[nx][ny] = 7  # 감시 표시

                nx += dx[d]
                ny += dy[d]

        # 조합 중 하나 탐색한 뒤 넘겨주기
        dfs(idx + 1, new_board)

dfs(0, office)
print(ans)