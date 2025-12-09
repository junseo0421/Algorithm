import sys
input = sys.stdin.readline
import heapq

heap = []
N = int(input())

for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap) * -1)
    else:
        heapq.heappush(heap, -x)