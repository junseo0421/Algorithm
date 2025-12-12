import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

apt = [input().rstrip() for _ in range(N)]
visited = [[False]*N for _ in range(N)]

result = []  # 각 단지 집의 수

def bfs(x, y):
    # 첫 (x, y) 부분이 apt = 1, visited 0 이라고 가정
    visited[x][y] = True

    q = deque()
    q.append([x, y])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    cnt = 1

    while q:
        a, b = q.popleft()

        for k in range(4):
            i = a + dx[k]
            j = b + dy[k]

            if i < 0 or i >= N or j < 0 or j >= N:
                continue

            if apt[i][j] == '1' and visited[i][j] == False:
                visited[i][j] = True
                cnt += 1
                q.append([i, j])

    result.append(cnt)

for i in range(N):
    for j in range(N):
        if apt[i][j] == '1' and visited[i][j] == False:
            bfs(i, j)

print(len(result))

for num in sorted(result):
    print(num)