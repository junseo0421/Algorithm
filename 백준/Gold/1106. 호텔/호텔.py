import sys
input = sys.stdin.readline

C, N = map(int, input().split())

hotel = [(0, 0)]

for _ in range(N):
    hotel.append(tuple(map(int, input().split())))

INF = float('inf')
dp = [[INF] * (C + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    cost, customer = hotel[i][0], hotel[i][1]

    for j in range(1, C + 1):
        dp[i][j] = dp[i-1][j]  # 해당 호텔을 포함하지 않았을 경우

        k = 0

        while j - k * customer > 0:  # 최소 손님 수가 채워지지 않았을 경우
            dp[i][j] = min(dp[i][j], dp[i-1][j - k * customer] + k * cost)
            k += 1

        dp[i][j] = min(dp[i][j], k * cost)

print(dp[N][C])