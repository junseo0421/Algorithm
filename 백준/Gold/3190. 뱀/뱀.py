import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 2  # 사과 : 2

L = int(input())

dir_lst = [''] * 10001
for _ in range(L):
    X, C = input().split()
    dir_lst[int(X)] = C

sec = 1

q = deque()
q.append((0, 0))
board[0][0] = 1

# 처음 머리는 오른쪽(동쪽)
dir = 1

while True:
    # 방향에 따라 머리 다음 칸 위치
    # 0, 1, 2, 3: 북, 동, 남, 서 순
    if dir == 0:
        x, y = q[-1][0] - 1, q[-1][1]
    elif dir == 1:
        x, y = q[-1][0], q[-1][1] + 1
    elif dir == 2:
        x, y = q[-1][0] + 1, q[-1][1]
    else:
        x, y = q[-1][0], q[-1][1] - 1

    # 머리가 위치한 칸이 벽인 지 확인
    if not (0 <= x < N and 0 <= y < N):
        break

    # 머리가 위치한 칸이 자기 몸인 지 확인
    if board[x][y] == 1:
        break

    q.append((x, y))

    # 사과 없으면 꼬리 자르기
    if board[x][y] != 2:
        x_remove, y_remove = q.popleft()
        board[x_remove][y_remove] = 0

    # 머리 위치한 칸 board 표시 (사과 or 벽 판정 후)
    board[x][y] = 1

    # 방향 반영
    if dir_lst[sec] == '':
        sec += 1
        continue
    else:
        if dir_lst[sec] == 'L':
            dir = (dir - 1) % 4
        else:
            dir = (dir + 1) % 4

    sec += 1

sys.stdout.write(str(sec))