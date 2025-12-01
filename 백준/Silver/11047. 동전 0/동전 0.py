import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coin_list = []

for _ in range(N):
    coin_list.append(int(input()))

cnt = 0

for coin in coin_list[::-1]:
    if coin > K:
        continue
    if K == 0:
        break

    cnt += K // coin
    K = K - (K // coin) * coin

sys.stdout.write(str(cnt))
