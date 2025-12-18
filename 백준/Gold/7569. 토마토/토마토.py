import sys
input = sys.stdin.readline

from collections import deque

M, N, H = map(int, input().split())

padding = M+2

layer_stride = padding * (N+2)

tomato = [-1] * layer_stride

for _ in range(H):
    tomato += [-1] * padding

    for _ in range(N):
        tomato += [-1] + list(map(int, input().split())) + [-1]

    tomato += [-1] * padding

tomato += [-1] * layer_stride

def bfs(x):  # x는 tomato가 1인 곳의 index lst
    q = deque(x)

    while q:
        a = q.popleft()

        for num in (a-1, a+1, a+padding, a-padding, a+layer_stride, a-layer_stride):
            if tomato[num] == 0:
                tomato[num] = tomato[a] + 1
                q.append(num)

one_lst = []

for idx, i in enumerate(tomato):
    if i == 1:
        one_lst.append(idx)

bfs(one_lst)

orig_tomato = []

for z in range(1, H+1):
    for r in range(1, N+1):
        for c in range(1, M+1):
            idx = z*layer_stride + r*padding + c
            orig_tomato.append(tomato[idx])

if len(one_lst) == 0 and 0 not in orig_tomato:
    sys.stdout.write('0')
    exit()

max_num = 1

for num in orig_tomato:
    if num == 0:
        sys.stdout.write('-1')
        exit()

    max_num = max(max_num, num)

sys.stdout.write(str(max_num - 1))
