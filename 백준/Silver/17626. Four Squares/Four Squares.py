import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

for i in range(1, N+1):
    dp[i] = i  # 최악의 경우로 초기화 (1로만 합이 이루어짐)
    j = 1
    
    while j*j <= i:
        dp[i] = min(dp[i], dp[i - j*j] + 1)
        j += 1

sys.stdout.write(str(dp[N]))
