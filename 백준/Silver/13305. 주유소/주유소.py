import sys
input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

result = 0
prev = 1e10

for r, p in zip(roads, prices):
    if p >= prev:  # 다음 도시가 기름값이 더 비쌀 때
        result += prev * r
    else:  # 해당 도시가 기름값이 이전보다 더 싼 게 나왔을 때
        result += p * r
        prev = p

print(result)