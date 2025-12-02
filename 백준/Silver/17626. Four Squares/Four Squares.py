import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

k = 1
while k*k <= N:
    dp[k*k] = 1
    k += 1

for i in range(1, N+1):
    if dp[i] != 0:  # 완전 제곱수 스킵
        continue

    j = 1
    while j*j < i:
        if dp[i] == 0:
            dp[i] = dp[j*j] + dp[i - j*j]
        else:
            dp[i] = min(dp[i], dp[j*j] + dp[i - j*j])
        j += 1

sys.stdout.write(str(dp[N]))
