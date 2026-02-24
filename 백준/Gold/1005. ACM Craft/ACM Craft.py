import sys
input = sys.stdin.readline

from collections import deque

# 위상 정렬

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    time = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]

    dp = [0] * (N+1)
    indegree = [0] * (N+1)

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1

    W = int(input())

    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i - 1]

    while q:
        node = q.popleft()

        for n in graph[node]:
            dp[n] = max(dp[n], dp[node] + time[n - 1])
            indegree[n] -= 1

            if indegree[n] == 0:
                q.append(n)

    sys.stdout.write(str(dp[W]) + '\n')