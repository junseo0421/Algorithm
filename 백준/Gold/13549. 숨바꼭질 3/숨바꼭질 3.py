import sys
input = sys.stdin.readline

from collections import deque

MAX_N = 100000

N, K = map(int, input().split())
visited = [-1] * (MAX_N + 1)

q = deque([N])
visited[N] = 0

if N > K:
    print(N - K)
    exit()

while q:
    num = q.popleft()

    if num == K:
        print(visited[num])
        break

    if num > K:
        if 0 <= (num - 1) <= MAX_N and visited[num - 1] == -1:
            visited[num - 1] = visited[num] + 1
            q.append(num - 1)
    else:
        nx = num * 2
        if 0 <= nx <= MAX_N and (visited[nx] == -1 or visited[nx] > visited[num]):
            visited[nx] = visited[num]
            q.appendleft(nx)

        for n in (num+1, num-1):
            if 0 <= n <= MAX_N and visited[n] == -1:
                visited[n] = visited[num] + 1
                q.append(n)