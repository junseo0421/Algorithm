import sys
input = sys.stdin.readline

C, N = map(int, input().split())
INF = float('inf')

# 비용으로 얻을 수 잇는 고객의 수가 100보다 작거나 같음
# C=1 일 때, 비용 1에 대한 인원수가 100 이라면, dp[100] = 1
dp = [INF] * (C+100)
dp[0] = 0  # 0명일 때는 비용이 0

# dp의 index는 고객의 수
# 해당 index에 대한 값 (비용)

for _ in range(N):
    cost, benefit = map(int, input().split())

    for i in range(benefit, C+100):
        dp[i] = min(dp[i], dp[i-benefit]+cost)

sys.stdout.write(str(min(dp[C:])))
