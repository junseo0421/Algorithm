import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())
MAX = 100000

def bfs(n, k):
    # 딕셔너리에서의 in 비용보다 list에서의 index로 처리하는 것이 더 빠름
    dist = [-1] * (MAX+1)
    ways = [0] * (MAX+1)

    q = deque([n])
    dist[n] = 0
    ways[n] = 1

    while q:
        num = q.popleft()

        # k의 최단 거리가 확정된 뒤, 그보다 깊은 level은 볼 필요 없으므로 break
        if dist[k] != -1 and dist[num] > dist[k]:
            break

        if num > k:
            minus = num - 1
            if not 0 <= minus <= MAX:
                continue

            if dist[minus] == -1:
                dist[minus] = dist[num] + 1
                ways[minus] = ways[num]
                q.append(minus)
            elif dist[minus] == dist[num] + 1:
                ways[minus] += ways[num]

        else:
            for i in (num-1, num+1, num*2):
                if not 0 <= i <= MAX:
                    continue

                if dist[i] == -1:
                    dist[i] = dist[num] + 1
                    ways[i] = ways[num]
                    q.append(i)
                elif dist[i] == dist[num] + 1:
                    ways[i] += ways[num]

    sys.stdout.write(str(dist[k]) + '\n' + str(ways[k]))

bfs(N, K)