import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

for i in range(N):
    T, P = map(int, input().split())

    if i+T > N:
        continue

    dp[i+T] = max(dp[i+T], max(dp[:i+1]) + P)

sys.stdout.write(str(max(dp)))