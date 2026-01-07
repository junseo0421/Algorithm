import sys
input = sys.stdin.readline

from collections import deque

# bfs 가 가장 빠를 듯?

N, K = map(int, input().split())

q = deque([N])

cnt_dict = {}
cnt_dict[N] = 0

while q:
    num = q.popleft()

    if num == K:
        sys.stdout.write(str(cnt_dict[num]))
        break

    if num > K:
        if num-1 not in cnt_dict:
            cnt_dict[num-1] = cnt_dict[num] + 1
            q.append(num-1)
    else:
        for i, x in enumerate((num*2, num-1, num+1)):
            if x not in cnt_dict:
                if i == 0:
                    cnt_dict[x] = cnt_dict[num]
                else:
                    cnt_dict[x] = cnt_dict[num] + 1
                q.append(x)

