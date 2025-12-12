import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())

q = deque([N])

cnt_dict = {N: 0}

while q:
    num = q.popleft()

    if num == K:
        print(cnt_dict[num])
        break
        
    if num > K:
        if num-1 not in cnt_dict:
            cnt_dict[num-1] = cnt_dict[num] + 1
            q.append(num-1)
    else:
        for i in (num-1, num+1, num*2):
            if i not in cnt_dict:
                cnt_dict[i] = cnt_dict[num] + 1
                q.append(i)
