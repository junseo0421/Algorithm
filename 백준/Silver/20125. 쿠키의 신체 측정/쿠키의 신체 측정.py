import sys
input = sys.stdin.readline

N = int(input())

board = [input().rstrip() for _ in range(N)]

is_head = 0
heart = (0, 0)

for i in range(N):
    for j in range(N):
        if board[i][j] == '*':
            is_head = 1
            heart = (i + 1, j)
            print(heart[0] + 1, heart[1] + 1)
            break

    if is_head:
        break

left_arm = right_arm = waist = left_leg = right_leg = 0

for i in range(heart[1]-1, -1, -1):
    if board[heart[0]][i] == '*':
        left_arm += 1
    else:
        break

for i in range(heart[1]+1, N):
    if board[heart[0]][i] == '*':
        right_arm += 1
    else:
        break

for i in range(heart[0] + 1, N):
    if board[i][heart[1]] == '*':
        waist += 1
    else:
        break

for i in range(heart[0] + waist + 1, N):
    if board[i][heart[1] - 1] == '*':
        left_leg += 1
    else:
        break

for i in range(heart[0] + waist + 1, N):
    if board[i][heart[1] + 1] == '*':
        right_leg += 1
    else:
        break

print(left_arm, right_arm, waist, left_leg, right_leg)