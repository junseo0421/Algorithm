import sys
input = sys.stdin.readline

from heapq import heappop, heappush

# 최단 경로는 다익스트라 알고리즘 사용
N, E = map(int, input().split())

INF = 1e9

# 각 그래프 연결
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

v1, v2 = map(int, input().split())

# 해당 정점에서 연결된 노드 순회 / heappop 으로 가장 작은 거리부터 순회
def dijkstra(start):
    dist_lst = [INF] * (N + 1)

    heap = []

    heappush(heap, (0, start))  # 누적 거리, 시작 노드
    dist_lst[start] = 0

    while heap:
        d, node = heappop(heap)

        if dist_lst[node] < d:
            continue

        for i in graph[node]:
            if d+i[1] < dist_lst[i[0]]:  # 옮긴 node의 dist 값이 누적된 dist 값보다 크다면 업데이트
                dist_lst[i[0]] = d+i[1]
                heappush(heap, (d+i[1], i[0]))

    return dist_lst


# 1번 start, v1 start, v2 start 로 다익스트라 3번 돌린 후 각 후보 경로 길이를 더하여 구할 수 있다.
lst_1 = dijkstra(1)
lst_v1 = dijkstra(v1)
lst_v2 = dijkstra(v2)

# 1 > v1 > v2 > N
cond1 = (lst_1[v1] == INF or lst_v1[v2] == INF or lst_v2[N] == INF)  # 중간 구간 중 하나라도 INF면 True
# 1 > v2 > v1 > N
cond2 = (lst_1[v2] == INF or lst_v2[v1] == INF or lst_v1[N] == INF)

if cond1 and cond2:  # 두 후보 경로 모두 불가능이면 -1 출력
    sys.stdout.write(str(-1))
else:
    result1 = lst_1[v1] + lst_v1[v2] + lst_v2[N]
    result2 = lst_1[v2] + lst_v2[v1] + lst_v1[N]
    sys.stdout.write(str(min(result1, result2)))
