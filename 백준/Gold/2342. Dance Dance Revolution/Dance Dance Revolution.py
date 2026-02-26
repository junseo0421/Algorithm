import sys
input = sys.stdin.readline

num_lst = list(map(int, input().split()))

# dp 상태 정의 dp[i][l][r] : i 번째 지시까지 처리했을 때, 왼발이 l, 오른발이 r에 있는 상태로 만드는 최소 누적 비용
INF = float('inf')

length = len(num_lst)

dp = [[INF] * 5 for _ in range(5)]

dp[0][0] = 0


def move(fr, to):
    if fr == to:
        return 1
    elif fr == 0:
        return 2
    elif abs(fr - to) == 2:
        return 4
    else:
        return 3


for x in range(length - 1):
    num = num_lst[x]
    nxt = [[INF] * 5 for _ in range(5)]

    for l in range(5):
        for r in range(5):
            nxt[num][r] = min(nxt[num][r], dp[l][r] + move(l, num))
            nxt[l][num] = min(nxt[l][num], dp[l][r] + move(r, num))

    dp = nxt

sys.stdout.write(str(min(map(min, dp))))