import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = []

for _ in range(N):
    house.append(int(input()))

house.sort()

left, right = 0, house[-1] - house[0]

while left <= right:
    mid = (left + right) // 2

    # 공유기를 mid 이상으로 설치 가능한 지 여부
    router = 1
    prev = house[0]  # 처음 집에는 무조건 설치

    for h in house[1:]:
        if h - prev >= mid:
            router += 1
            prev = h

    if router >= C:  # C개 이상의 공유기 설치 가능
        left = mid + 1
    else:
        right = mid - 1

print(right)