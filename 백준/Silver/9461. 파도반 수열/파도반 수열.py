import sys
input = sys.stdin.readline

T = int(input())

MAX_N = 100

dp = [0] * (MAX_N + 1)
dp[1:3] = [1, 1]

for i in range(3, MAX_N + 1):
    dp[i] = dp[i-3] + dp[i-2]
    
for _ in range(T):
    print(dp[int(input())])