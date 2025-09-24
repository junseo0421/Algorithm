import sys

N, M = map(int, sys.stdin.readline().split())

basket_list = []

for num in range(1, N+1):
    basket_list.append(num)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    basket_list[i-1:j] = basket_list[i-1:j][::-1]

print(*basket_list)
