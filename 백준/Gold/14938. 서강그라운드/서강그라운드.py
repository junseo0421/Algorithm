import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
t_lst = list(map(int, input().split()))

INF = 1e9
matrix = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    matrix[a][b] = min(matrix[a][b], l)
    matrix[b][a] = min(matrix[b][a], l)

for i in range(1, n+1):
    matrix[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

result = 0

for i in range(1, n+1):
    row_sum = 0

    for j in range(1, n+1):
        if matrix[i][j] <= m:
            row_sum += t_lst[j-1]

    result = max(result, row_sum)

sys.stdout.write(str(result))
