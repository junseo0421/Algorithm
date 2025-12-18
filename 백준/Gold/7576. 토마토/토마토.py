import sys
input = sys.stdin.readline

from collections import deque

M, N = map(int, input().split())

padding = M+2

tomato = [-1] * padding

for _ in range(N):
    tomato += [-1] + list(map(int, input().split())) + [-1]

tomato += [-1] * padding

def bfs(lst):  # 1인 index가 들어있는 list를 인수로 받음
    q = deque(lst)

    while q:
        a = q.popleft()

        for num in (a+1, a-1, a+padding, a-padding):
            if tomato[num] == 0:
                tomato[num] = tomato[a] + 1
                q.append(num)

one_lst = []

for idx, i in enumerate(tomato):
    if i == 1:
        one_lst.append(idx)

bfs(one_lst)

orig_tomato = []

for r in range(1, N+1):
    for c in range(1, M+1):
        idx = r*padding + c
        orig_tomato.append(tomato[idx])

if len(one_lst) == 0 and 0 not in orig_tomato:
    sys.stdout.write('0')
    exit()

max_num = 1

for t in orig_tomato:
    if t == 0:
        sys.stdout.write('-1')
        exit()

    max_num = max(max_num, t)

sys.stdout.write(str(max_num - 1))
