import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

visited = [-1] * 101

# stair = {}
# snake = {}
#
# for _ in range(N):
#     a, b = map(int, input().split())
#     stair[a] = b
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     snake[a] = b


stair_snake = {}

for _ in range(M+N):
    a, b = map(int, input().split())
    stair_snake[a] = b

def bfs(n):
    q = deque([n])

    visited[n] = 0

    while q:
        a = q.popleft()

        if a == 100:
            sys.stdout.write(str(visited[a]))
            break

        for k in range(1, 7):
            num = a + k

            if num > 100:
                continue

            if num in stair_snake:
                next = stair_snake[num]
            else:
                next = num

            if visited[next] == -1:
                q.append(next)
                visited[next] = visited[a] + 1

bfs(1)