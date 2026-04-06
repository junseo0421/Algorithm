import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')
dp = [[[INF] * 3 for _ in range(M)] for _ in range(N)]  # 0, 1, 2 방향으로 내려왔을 때의 최소 연료

# 초기값 설정
for c in range(M):
    dp[0][c][0] = lst[0][c]
    dp[0][c][1] = lst[0][c]
    dp[0][c][2] = lst[0][c]

for i in range(1, N):
    for j in range(M):
        if 0 <= j+1 < M:
            dp[i][j][0] = lst[i][j] + min(dp[i-1][j+1][1], dp[i-1][j+1][2])

        dp[i][j][1] = lst[i][j] + min(dp[i-1][j][0], dp[i-1][j][2])

        if 0 <= j-1 < M:
            dp[i][j][2] = lst[i][j] + min(dp[i-1][j-1][0], dp[i-1][j-1][1])

ans = INF

for c in range(M):
    for d in range(3):
        ans = min(ans, dp[-1][c][d])

print(ans)