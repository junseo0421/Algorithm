import sys
input = sys.stdin.readline

import heapq

heap = []

N = int(input())

for _ in range(N):
    num = int(input())

    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)

    else:
        heapq.heappush(heap, num)
