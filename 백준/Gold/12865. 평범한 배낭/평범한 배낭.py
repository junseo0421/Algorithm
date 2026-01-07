import sys
input = sys.stdin.readline

# 경우의 수는 물건을 넣는다/안 넣는다
# dp[w] = 무게 한도 w에서 가능한 최대 가치

N, K = map(int, input().split())

dp = [0] * (K+1)

for _ in range(N):
    W, V = map(int, input().split())
    for w in range(K, W-1, -1):
        dp[w] = max(dp[w], dp[w-W] + V)

sys.stdout.write(str(dp[K]))