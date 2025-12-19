import sys
input = sys.stdin.readline

from heapq import heappush, heappop

T = int(input())

def is_empty(dict):
    for d in dict:
        if d[1] > 0:
            return False
    return True

for _ in range(T):
    k = int(input())
    min_heap, max_heap = [], []
    num_dict = {}

    for _ in range(k):
        o, n = input().split()
        n = int(n)

        if o == 'I':
            if n in num_dict:
                num_dict[n] += 1
            else:
                num_dict[n] = 1
                heappush(min_heap, n)
                heappush(max_heap, -n)

        else:  # 삭제
            if not is_empty(num_dict.items()):
                if n == 1:  # 최댓값 삭제
                    while -max_heap[0] not in num_dict or num_dict[-max_heap[0]] < 1:  # dictionary에 없거나 dict cnt가 0인 경우 모두 삭제
                        temp = -heappop(max_heap)
                        if temp in num_dict:  # dict 엔 있는데 cnt가 0인 경우
                            del num_dict[temp]  # dictionary 길이 줄이기
                    num_dict[-max_heap[0]] -= 1  # 삭제는 while 문에서 먼저 실행됨

                else:  # 최솟값 삭제
                    while min_heap[0] not in num_dict or num_dict[min_heap[0]] < 1:
                        temp = heappop(min_heap)
                        if temp in num_dict:
                            del num_dict[temp]
                    num_dict[min_heap[0]] -= 1

    if is_empty(num_dict.items()):
        sys.stdout.write('EMPTY\n')
    else:
        while -max_heap[0] not in num_dict or num_dict[-max_heap[0]] < 1:
            heappop(max_heap)
        while min_heap[0] not in num_dict or num_dict[min_heap[0]] < 1:
            heappop(min_heap)
        sys.stdout.write(str(-max_heap[0]) + ' ' + str(min_heap[0]) + '\n')