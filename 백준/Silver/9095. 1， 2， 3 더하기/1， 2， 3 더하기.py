import sys
input = sys.stdin.readline

T = int(input())

num_list = [1, 2, 3]
MAX_N = 10
dp = [0] * (MAX_N + 1)

for i in range(1, MAX_N+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    elif i == 3:
        dp[i] = 4
    else:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
for _ in range(T):
    print(dp[int(input())])
