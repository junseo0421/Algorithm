import sys
input = sys.stdin.readline

sudoku = [list(map(int, input().rstrip())) for _ in range(9)]

zero_index = []

# row, col, box [r][n] → r번째 row, col, box 에 n 이 존재하나, 안 하나
row = [[False] * 9 for _ in range(9)]
col = [[False] * 9 for _ in range(9)]
box = [[False] * 9 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero_index.append((i, j))
        else:
            num = sudoku[i][j] - 1  # index 로 변환
            row[i][num] = True
            col[j][num] = True
            box[i // 3 * 3 + j // 3][num] = True


def back(idx):  # 0 의 index 를 받기
    if idx == len(zero_index):
        return True

    x, y = zero_index[idx]

    for n in range(9):
        if not row[x][n] and not col[y][n] and not box[x // 3 * 3 + y // 3][n]:
            sudoku[x][y] = n + 1
            row[x][n], col[y][n], box[x // 3 * 3 + y // 3][n] = True, True, True
            if back(idx + 1):
                return True
            row[x][n], col[y][n], box[x // 3 * 3 + y // 3][n] = False, False, False
            sudoku[x][y] = 0

    return False

back(0)

for i in range(9):
    sys.stdout.write(''.join(map(str, sudoku[i])) + '\n')