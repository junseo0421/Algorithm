import sys
input = sys.stdin.readline

N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]

presum = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        presum[i][j] = table[i-1][j-1] + presum[i-1][j] + presum[i][j-1] - presum[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    result = presum[x2][y2] - presum[x2][y1-1] - presum[x1-1][y2] + presum[x1-1][y1-1]

    sys.stdout.write(str(result) + '\n')

