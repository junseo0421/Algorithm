import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(3)
else:
    dp = [0] * (N + 1)

    dp[1] = 1
    dp[2] = 4  # 누적합으로

    for i in range(3, N + 1):
        if i % 2 == 1: # 홀수
            dp[i] = dp[i-1] * 2 + 1
        else:
            dp[i] = dp[i-1] * 2 + 2

    print((dp[N] // 2 + 1) % 10007)
