import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())

fibo_mat = [[1, 1], [1, 0]]
zero = [[0, 0], [0, 0]]
mod = 1000000007

def matmul(a, b):
    new_matrix = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                new_matrix[i][j] += (a[i][k] % mod) * (b[k][j] % mod) % mod

    return new_matrix

def conquer_square(x, n):
    if n == 0:
        return zero
    if n == 1:
        return x

    temp = conquer_square(x, n // 2)

    if n % 2 == 0:
        return matmul(temp, temp)
    else:
        return matmul(matmul(temp, temp), x)


result_mat = conquer_square(fibo_mat, N)

sys.stdout.write(str(result_mat[1][0] % mod))