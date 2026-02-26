import sys
input = sys.stdin.readline

from collections import deque

# 위상 정렬을 활용해야한다.
# 사이클이 존재하는 경우도 고려해야함.
# 사이클에 존재하면 모든 노드가 큐에 들어가지 않을 것임.

N, M = map(int, input().split())
indegree_lst = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
result = []

for _ in range(M):
    singers = list(map(int, input().split()))

    for i in range(1, singers[0]):
        graph[singers[i]].append(singers[i+1])
        indegree_lst[singers[i+1]] += 1


q = deque()

for i in range(1, N+1):
    if indegree_lst[i] == 0:
        q.append(i)

while q:
    n = q.popleft()
    result.append(n)

    for node in graph[n]:
        indegree_lst[node] -= 1

        if indegree_lst[node] == 0:
            q.append(node)

if len(result) == N:
    sys.stdout.write('\n'.join(map(str, result)))
else:
    sys.stdout.write('0')