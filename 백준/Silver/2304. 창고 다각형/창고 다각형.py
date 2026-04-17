import sys
input = sys.stdin.readline

N = int(input())
pillars = []
max_h = 0
ans = 0

for _ in range(N):
    L, H = map(int, input().split())
    max_h = max(max_h, H)
    pillars.append((L, H))

if N == 1:
    print(pillars[0][1])
    exit()

pillars.sort()

left = []
right = []
max_left_l = max_right_r = 0

for x in pillars:
    l, h = x

    if h == max_h:
        max_left_l = l
        left.append(x)
        break

    left.append(x)

for x in pillars[::-1]:
    l, h = x

    if h == max_h:
        max_right_r = l
        right.append(x)
        break

    right.append(x)

if len(left) > 1:
    left_max_idx = left[0]

    for l, h in left[1:]:
        if h > left_max_idx[1]:
            ans += (l - left_max_idx[0]) * left_max_idx[1]
            left_max_idx = (l, h)

if len(right) > 1:
    right_max_idx = right[0]

    for l, h in right[1:]:
        if h > right_max_idx[1]:
            ans += (right_max_idx[0] - l) * right_max_idx[1]
            right_max_idx = (l, h)

ans += (max_right_r - max_left_l + 1) * max_h

print(ans)