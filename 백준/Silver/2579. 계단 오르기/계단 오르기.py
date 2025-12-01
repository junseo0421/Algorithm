import sys
input = sys.stdin.readline

N = int(input())

step_list = [int(input()) for _ in range(N)]

dp = [0] * N

if len(step_list) <= 2:
    sys.stdout.write(str(sum(step_list)))
else:
    dp[0] = step_list[0]
    dp[1] = step_list[0] + step_list[1]
    for i in range(2, N):
        dp[i] = max(dp[i-3] + step_list[i-1] + step_list[i], dp[i-2] + step_list[i])

    sys.stdout.write(str(dp[-1]))
    