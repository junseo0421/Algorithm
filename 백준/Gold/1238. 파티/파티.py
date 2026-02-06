import sys
input = sys.stdin.readline

from heapq import heappush, heappop

# 오는 것과 가는 것 모두 구해야함.
# 다익스트라 : 한 정점에서 각 정점들까지의 최단 거리
# 플로이드-워셜 : 모든 정점에서 각 정점들까지의 최단 거리

# 다익스트라로 모든 N 을 구현하되, 가지치기 도입

N, M, X = map(int, input().split())

INF = float('inf')
graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())

    # 시작점과 끝점이 같은 도로는 없음, 단방향 도로
    # 우선 순위 큐 (힙) 사용을 위해 cost 먼저 넣어주기
    graph[start].append((cost, end))

result = [0]

for i in range(1, N+1):
    dist = [INF] * (N+1)

    heap = [(0, i)]

    while heap:
        c, n = heappop(heap)

        if n == X:
            result.append(c)
            break

        for cost, node in graph[n]:
            if dist[node] < cost:
                continue

            if c + cost < dist[node]:
                dist[node] = c + cost
                heappush(heap, (c + cost, node))

dist = [INF] * (N+1)

heap = [(0, X)]

while heap:
    c, n = heappop(heap)

    for cost, node in graph[n]:
        if dist[node] < cost:
            continue

        if c + cost < dist[node]:
            dist[node] = c + cost
            heappush(heap, (c + cost, node))

dist[X] = 0

max_result = 0

for i in range(1, N+1):
    max_result = max(max_result, result[i] + dist[i])

sys.stdout.write(str(max_result))