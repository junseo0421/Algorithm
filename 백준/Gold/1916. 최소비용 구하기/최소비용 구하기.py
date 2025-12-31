import sys
input = sys.stdin.readline

from heapq import heappop, heappush

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

dist = [1e18] * (N+1)
dist[start] = 0

heap = [(0, start)]  # 간선비용 (누적 비용이 들어가야함), 시작 노드

while heap:
    cost, node = heappop(heap)

    if cost > dist[node]:
        continue

    if node == end:
        break

    for dest, per_cost in graph[node]:
        nc = cost + per_cost
        if nc < dist[dest]:
            dist[dest] = nc
            heappush(heap, (nc, dest))

sys.stdout.write(str(dist[end]))
