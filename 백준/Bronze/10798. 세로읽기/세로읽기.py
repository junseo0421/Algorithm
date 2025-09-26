import sys

matrix = []

for _ in range(5):
    row = sys.stdin.readline().rstrip()
    matrix.append(list(row))

max_len = max(len(row) for row in matrix)

output = []

for j in range(max_len):
    for i in range(5):
        if j < len(matrix[i]):
            output.append(matrix[i][j])

print(''.join(output))
