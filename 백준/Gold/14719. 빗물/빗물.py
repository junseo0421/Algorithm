import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

max_h = max(blocks)
max_hl = blocks.index(max_h)

lst = list(zip(range(W), blocks))

ans = 0

S = 0

for i in range(max_hl):
    l, h = lst[i]

    if h > S:
        S = h
    else:
        ans += S - h

S = 0

for j in range(W-1, max_hl, -1):
    l, h = lst[j]

    if h > S:
        S = h
    else:
        ans += S - h

print(ans)