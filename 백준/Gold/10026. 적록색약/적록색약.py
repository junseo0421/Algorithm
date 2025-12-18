import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

padding = N+2

color = ['0'] * padding

for _ in range(N):
    color += ['0'] + list(input().rstrip()) + ['0']

color += ['0'] * padding

color2 = ['R' if x == 'G' else x for x in color]

visited1 = [0] * padding * padding
visited2 = [0] * padding * padding

def bfs(x, arr, visit):
    q = deque([x])

    visit[x] = 1  # 숫자로 대체

    while q:
        a = q.popleft()

        for num in (a+1, a-1, a+padding, a-padding):
            if visit[num] != 0:
                continue
            if arr[num] == arr[a]:  # 같은 색이어야함;
                visit[num] = 1
                q.append(num)

cnt1 = 0
cnt2 = 0

for r in range(1, N+1):
    for c in range(1, N+1):
        idx = r * padding + c
        if visited1[idx] == 0:
            bfs(idx, color, visited1)
            cnt1 += 1

        if visited2[idx] == 0:
            bfs(idx, color2, visited2)
            cnt2 += 1

sys.stdout.write(str(cnt1) + " " + str(cnt2))