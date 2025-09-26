import sys

N, M = map(int, sys.stdin.readline().split())

matrix_A, matrix_B = [], []

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    matrix_A.append(row)

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    matrix_B.append(row)

result = []
for i in range(N):
    row_result = []
    for j in range(M):
        row_result.append(matrix_A[i][j] + matrix_B[i][j])

    result.append(row_result)

for row in result:
    print(*row)
