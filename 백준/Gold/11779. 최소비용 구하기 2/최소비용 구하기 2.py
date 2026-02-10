import sys
input = sys.stdin.readline

from heapq import heappop, heappush

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append((cost, e))

start, end = map(int, input().split())

INF = float('inf')
dist = [INF] * (n+1)

heap = []
prev = [0] * (n+1)

heappush(heap, (0, start))
dist[start] = 0

while heap:
    total_cost, node = heappop(heap)

    if node == end:  # 종료 조건
        break

    if dist[node] < total_cost:  # 가지 치기
        continue

    for tc, next_node in graph[node]:
        if total_cost + tc < dist[next_node]:
            dist[next_node] = total_cost + tc
            prev[next_node] = node
            heappush(heap, (total_cost + tc, next_node))

sys.stdout.write(str(dist[end]) + '\n')

result = [end]

while True:
    end = prev[end]
    result.append(end)

    if end == start:
        break

sys.stdout.write(str(len(result)) + '\n')
sys.stdout.write(" ".join(map(str, result[::-1])))