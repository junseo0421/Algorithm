# cnfcj : https://velog.io/@highcho/Algorithm-baekjoon-11286

import sys
input = sys.stdin.readline
import heapq

N = int(input())

heap = []

for _ in range(N):
    num = int(input())
    
    if num:
        heapq.heappush(heap, (abs(num), num))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
            