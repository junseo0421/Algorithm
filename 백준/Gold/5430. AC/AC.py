import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

## 최대한 reverse 연산을 줄여보자

for _ in range(T):
    order = input().rstrip()
    n = int(input())

    if n == 0:
        _ = input()
        q = deque()
    elif n == 1:
        q = deque([int(input().rstrip()[1:-1])])
    else:
        q = deque(list(map(int, input().rstrip()[1:-1].split(','))))

    is_error = False

    r_cnt = 0

    for o in order:
        if o == 'R':
            r_cnt += 1
        else:  # d 일 때
            if len(q) == 0:
                sys.stdout.write('error' + '\n')
                is_error = True
                break
            if r_cnt % 2 == 1:
                q.pop()
            else:
                q.popleft()

    if r_cnt % 2 == 1:
        q.reverse()
    if is_error:
        continue
    elif len(q) == 0:
        sys.stdout.write('[]' + '\n')
    else:
        sys.stdout.write('[' + ','.join(map(str, q)) + ']' + '\n')
