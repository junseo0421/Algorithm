import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

maze = [input().rstrip() for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

def bfs(x, y):
    q = deque()
    q.append([x, y])

    visited[x][y] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        a, b = q.popleft()

        if a == N - 1 and b == M - 1:
            sys.stdout.write(str(visited[a][b] + 1))
            return

        for k in range(4):
            i = a + dx[k]
            j = b + dy[k]
            
            if i < 0 or i >= N or j < 0 or j >= M:
                continue

            if visited[i][j] == -1 and maze[i][j] == '1':
                visited[i][j] = visited[a][b] + 1
                q.append([i, j])

                

bfs(0, 0)
