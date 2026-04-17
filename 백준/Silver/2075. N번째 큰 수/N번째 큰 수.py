import sys
input = sys.stdin.readline

from heapq import heappop, heappush

heap = []

N = int(input())

for x in map(int, input().split()):
    heappush(heap, x)

for _ in range(N-1):
    for x in map(int, input().split()):
        temp = heappop(heap)
        if x > temp:
            heappush(heap, x)
        else:
            heappush(heap, temp)

print(heappop(heap))