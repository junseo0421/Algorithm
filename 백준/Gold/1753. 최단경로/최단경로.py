import sys
input = sys.stdin.readline

from heapq import heappop, heappush

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
INF = 1e9
dist_lst = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # 다음 노드, dist

def dijkstra(start):
    heap = []
    
    heappush(heap, (0, start))  # 누적 거리, 시작 노드
    dist_lst[start] = 0
    
    while heap:
        dist, node = heappop(heap)
        
        if dist_lst[node] < dist:
            continue
            
        for i in graph[node]:  # i[0]: 다음 노드, i[1]: 다음 노드까지의 dist
            if dist+i[1] < dist_lst[i[0]]:
                dist_lst[i[0]] = dist+i[1]
                heappush(heap, (dist+i[1], i[0]))
    
dijkstra(K)

for j in range(1, V+1):
    if dist_lst[j] == INF:
        sys.stdout.write('INF' + '\n')
        continue
    sys.stdout.write(str(dist_lst[j]) + '\n')
