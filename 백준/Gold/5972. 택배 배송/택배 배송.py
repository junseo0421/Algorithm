import sys
input = sys.stdin.readline

from heapq import heappop, heappush

# 다익스트라 문제

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, finish, cost = map(int, input().split())

    # 양방향, 하나 이상의 길 존재 가능
    graph[start].append((cost, finish))
    graph[finish].append((cost, start))

INF = float('inf')
dist = [INF] * (N + 1)

def dijkstra(start):
    heap = []
    heappush(heap, (0, start))  # 거리, 노드 번호
    dist[start] = 0

    while heap:
        d, node = heappop(heap)  # 가장 짧은 거리, 해당 노드

        if dist[node] < d:  # 힙에는 같은 노드가 여러 번 들어갈 수 있음
            continue

        for cost, next_node in graph[node]:
            # 현재 기록된 거리보다 다음 노드까지 가는 새 거리 후보가 작다면
            if d + cost < dist[next_node]:  
                dist[next_node] = d + cost
                heappush(heap, (dist[next_node], next_node))

dijkstra(1)

print(dist[N])