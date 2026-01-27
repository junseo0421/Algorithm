import sys
input = sys.stdin.readline

N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def matrix_product(a, b):
    X = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                X[i][j] += a[i][k] * b[k][j] % 1000

    return X

def square(x, n):
    if n == 1:  # 재귀가 끝까지 다 돌면 행렬 x 반환
        return x
    temp = square(x, n//2)

    if n % 2 == 0:  # 짝수이면
        return matrix_product(temp, temp)
    else:
        return matrix_product(matrix_product(temp, temp), x)

result = square(matrix, B)

for i in range(N):
    for j in range(N):
        result[i][j] %= 1000

for row in result:
    sys.stdout.write(" ".join(map(str, row)) + "\n")

