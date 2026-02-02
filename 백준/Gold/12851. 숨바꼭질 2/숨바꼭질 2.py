import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())
MAX = 100000

def bfs(n, k):
    dist = {}  # x까지 가는 최단 거리
    ways = {}  # 일반적인 bfs랑은 다르게 도달했던 노드도 전부 돌아야하기 때문에 방법의 수를 따로 두었음

    q = deque([n])
    dist[n] = 0
    ways[n] = 1

    while q:
        num = q.popleft()

        if num > k:
            minus = num - 1
            if not 0 <= minus <= MAX:
                continue

            if minus not in dist:
                dist[minus] = dist[num] + 1
                ways[minus] = ways[num]
                q.append(minus)
            elif dist[minus] == dist[num] + 1:
                ways[minus] += ways[num]

        else:
            for i in (num-1, num+1, num*2):
                if not 0 <= i <= MAX:
                    continue

                if i not in dist:
                    dist[i] = dist[num] + 1
                    ways[i] = ways[num]
                    q.append(i)
                elif dist[i] == dist[num] + 1:
                    ways[i] += ways[num]

    sys.stdout.write(str(dist[k]) + '\n')
    sys.stdout.write(str(ways[k]))

bfs(N, K)