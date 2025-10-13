import sys

m, n = map(int, sys.stdin.readline().split())

board = []
result = []

for _ in range(m):
    board.append([i for i in sys.stdin.readline().rstrip()])

for i in range(m-7):
    for j in range(n-7):
        start_b = 0
        start_w = 0

        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0:
                    if board[x][y] == 'W':
                        start_b += 1
                    else:
                        start_w += 1
                else:
                    if board[x][y] == 'W':
                        start_w += 1
                    else:
                        start_b += 1

        result.append(start_b)
        result.append(start_w)

print(min(result))
