import sys

matrix = []

for _ in range(100):
    matrix.append([0]*100)

N = int(sys.stdin.readline())
for _ in range(N):
    X, Y = map(int, sys.stdin.readline().split())

    for j in range(Y, Y+10):
        matrix[j][X:X+10] = [1]*10

print(sum(map(sum, matrix)))