import sys
input = sys.stdin.readline

num_lst = list(map(int, input().split()))

# dp 상태 정의 dp[l][r] : 지금까지의 입력들을 모두 처리한 뒤, 왼발이 l, 오른발이 r에 있는 상태로 만드는 최소 누적 비용
INF = float('inf')

length = len(num_lst)

# inf 는 아직 도달 못 한 부분
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

    # 새로운 상태를 담는 부분
    nxt = [[INF] * 5 for _ in range(5)]

    for l in range(5):
        for r in range(5):
            if dp[l][r] == INF:
                continue
            # 같은 새 상태 (a, b) 에 도달하는 경로가 여러 개일 수 있음
            nxt[num][r] = min(nxt[num][r], dp[l][r] + move(l, num))
            nxt[l][num] = min(nxt[l][num], dp[l][r] + move(r, num))

    dp = nxt

# 총 최소 비용 구하기
sys.stdout.write(str(min(map(min, dp))))