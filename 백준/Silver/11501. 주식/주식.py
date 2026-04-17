import sys
input = sys.stdin.readline

T = int(input())

# 앞으로 남은 날들 중 가장 비싼 날을 기준으로 보기

# 뒤에서부터 보면서
# 지금까지 본 가격 중 최댓값을 max_price로 유지
# 현재 가격이 max_price보다 작으면 오늘 사서 나중에 max_price에 판다고 생각
# 현재 가격이 max_price보다 크거나 같으면 그 날이 새로운 판매 기준일

for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))

    max_price = ans = 0

    for i in range(N-1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            ans += max_price - prices[i]

    print(ans)