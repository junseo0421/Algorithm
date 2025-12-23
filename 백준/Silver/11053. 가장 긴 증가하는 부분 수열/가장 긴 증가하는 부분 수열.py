import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

dp = [0] * N

dp[0] = 1

for i in range(1, N):
    max_j = 0

    for j in range(i):
        if lst[i] > lst[j]:
            max_j = max(dp[j], max_j)

    if max_j:
        dp[i] = max_j + 1
    else:
        dp[i] = 1

sys.stdout.write(str(max(dp)))
