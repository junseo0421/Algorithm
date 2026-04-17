import sys
input = sys.stdin.readline

# 1. 빨간색을 왼쪽으로 몰기
# 2. 파란색을 왼쪽으로 몰기
# 3. 빨간색을 오른쪽으로 몰기
# 4. 파란색을 오른쪽으로 몰기
# -> 최솟값

N = int(input())
balls = input().rstrip()
red = 0
blue = 0

for s in balls:
    if s == 'R':
        red += 1
    else:
        blue += 1

ans = 1e9

# 파란색을 왼쪽으로 몰기
cnt = 0

if balls[0] == 'R':
    ans = min(ans, blue)
else:
    for s in balls:
        if s == 'B':
            cnt += 1
        else:
            break

    ans = min(ans, blue - cnt)

# 빨간색을 왼쪽으로 몰기
cnt = 0

if balls[0] == 'B':
    ans = min(ans, red)
else:
    for s in balls:
        if s == 'R':
            cnt += 1
        else:
            break

    ans = min(ans, red - cnt)

# 파란색을 오른쪽으로 몰기
cnt = 0

if balls[-1] == 'R':
    ans = min(ans, blue)
else:
    for s in balls[::-1]:
        if s == 'B':
            cnt += 1
        else:
            break

    ans = min(ans, blue - cnt)

# 빨간색을 오른쪽으로 몰기
cnt = 0

if balls[-1] == 'B':
    ans = min(ans, red)
else:
    for s in balls[::-1]:
        if s == 'R':
            cnt += 1
        else:
            break

    ans = min(ans, red - cnt)

print(ans)