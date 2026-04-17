import sys
input = sys.stdin.readline

N, D = map(int, input().split())

road_dict = [[] for _ in range(D+1)]

for _ in range(N):
    start, finish, distance = map(int, input().split())
    if finish > D or finish - start <= distance:
        continue

    road_dict[start].append((finish, distance))

dp = [1e5] * (D+1)

dp[0] = 0

for i in range(D+1):
    dp[i] = min(dp[i - 1] + 1, dp[i])

    if road_dict[i]:
        for f, d in road_dict[i]:
            dp[f] = min(dp[f], dp[i] + d)

print(dp[D])