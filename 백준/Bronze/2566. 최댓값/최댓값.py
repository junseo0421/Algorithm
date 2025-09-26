import sys

matrix = []

for _ in range(9):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)

max_num = -1
max_row, max_col = 0, 0

for i in range(9):
    for j in range(9):
        if max_num < matrix[i][j]:
            max_num = matrix[i][j]
            max_row, max_col = i+1, j+1

print(max_num)
print(max_row, max_col)