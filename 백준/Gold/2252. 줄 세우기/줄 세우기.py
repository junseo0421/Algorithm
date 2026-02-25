import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

indegree_lst = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree_lst[B] += 1

q = deque()

for i in range(1, N+1):
    if indegree_lst[i] == 0:
        q.append(i)

while q:
    num = q.popleft()
    sys.stdout.write(str(num) + ' ')

    for nxt in graph[num]:
        indegree_lst[nxt] -= 1

        if indegree_lst[nxt] == 0:
            q.append(nxt)
