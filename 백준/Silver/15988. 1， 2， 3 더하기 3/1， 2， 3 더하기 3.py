import sys
input = sys.stdin.readline

T = int(input())
MAX_N = 1000000

dp = [0] * (MAX_N + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, MAX_N + 1):
    dp[i] += (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for _ in range(T):
    case = int(input())
    print(dp[case])