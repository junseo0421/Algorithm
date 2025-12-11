import sys
input = sys.stdin.readline

from collections import Counter

N, M, B = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(N)]

flat = sum(land, [])

height_cnt = Counter(flat)

min_h = min(height_cnt.keys())
max_h = max(height_cnt.keys())

best_time = 1e10
best_h = 0

for h in range(min_h, max_h + 1):
    removed = 0
    needed = 0
    time = 0

    for height, cnt in height_cnt.items():
        if height > h:  # 같은 경우는 포함 x
            diff = height - h
            removed += diff * cnt
            time += diff * cnt * 2
        elif height < h:
            diff = h - height
            needed += diff * cnt
            time += diff * cnt

    if removed + B >= needed:
        if time < best_time or (time == best_time and h > best_h):
            best_time = time
            best_h = h

print(best_time, best_h)
