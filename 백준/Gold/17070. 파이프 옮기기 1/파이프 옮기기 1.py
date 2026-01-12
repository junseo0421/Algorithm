import sys
input = sys.stdin.readline

N = int(input())

pipe_lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * N for _ in range(N)] for _ in range(3)]

# 각 3가지 상태를 dp로 지정
# dp[0][i][j] : (i, j)가 끝점이고 가로(→) 로 놓인 경우의 수
# dp[1][i][j] : (i, j)가 끝점이고 세로(↓) 로 놓인 경우의 수
# dp[2][i][j] : (i, j)가 끝점이고 대각(↘) 로 놓인 경우의 수

# 이동 규칙
# 1. 가로로 끝점이 i, j인 경우
# 가로/대각으로 와서 만들 수 있음
# [i][j] 가 비어야함
# dp[0][i][j-1] + dp[2][i][j-1]

# 2. 세로
# 세로/대각으로 와서 만들 수 있음
# [i][j] 가 비어야함
# dp[1][i-1][j] + dp[2][i-1][j]

# 3. 대각
# 세로/대각/가로로 만들 수 있음
# [i][j], [i-1][j], [i][j-1] 3칸이 비어야함
# dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

dp[0][0][1] = 1

for first_row in range(2, N):
    if pipe_lst[0][first_row] == 1:
        break

    dp[0][0][first_row] += dp[0][0][first_row-1]

for i in range(1, N):
    for j in range(1, N):
        if pipe_lst[i][j] == 0:
            dp[0][i][j] += dp[0][i][j-1] + dp[2][i][j-1]
            dp[1][i][j] += dp[1][i-1][j] + dp[2][i-1][j]

            if pipe_lst[i-1][j] == 0 and pipe_lst[i][j-1] == 0:
                dp[2][i][j] += dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

result = dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1]
sys.stdout.write(str(result))
