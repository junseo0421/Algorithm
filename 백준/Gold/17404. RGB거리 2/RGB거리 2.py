import sys
input = sys.stdin.readline

# 1 ≠ 2, 1 ≠ N, N ≠ N-1, i ≠ i-1, i ≠ i+1
# 1 ≠ N 의 조건을 어떻게 해야하지

N = int(input())
INF = float('inf')

result = INF

num_lst = [list(map(int, input().split())) for _ in range(N)]

for mask in range(3):
    dp = [[0] * 3 for _ in range(N)]

    dp[0] = num_lst[0][:]

    if mask == 0:
        dp[0][1] = dp[0][2] = INF
    elif mask == 1:
        dp[0][0] = dp[0][2] = INF
    else:
        dp[0][0] = dp[0][1] = INF

    for i in range(1, N):
        dp[i][0] = num_lst[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = num_lst[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = num_lst[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    if mask == 0:
        result = min(result, min(dp[N - 1][1], dp[N - 1][2]))
    elif mask == 1:
        result = min(result, min(dp[N - 1][0], dp[N - 1][2]))
    else:
        result = min(result, min(dp[N - 1][0], dp[N - 1][1]))

sys.stdout.write(str(result))