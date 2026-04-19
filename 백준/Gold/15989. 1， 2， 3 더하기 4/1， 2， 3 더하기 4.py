import sys
input = sys.stdin.readline

T = int(input())

dp = [0] * 10001
dp[0] = 1

for num in [1, 2, 3]:
    for i in range(num, 10001):
        dp[i] += dp[i - num]

for _ in range(T):
    case = int(input())
    print(dp[case])