import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    visited = ['x'] * 10000
    visited[a] = ''

    q = deque([a])

    while q:
        num = q.popleft()  # int

        if num == b:
            sys.stdout.write(visited[num] + '\n')
            break

        # D
        d = num * 2 % 10000
        if visited[d] == 'x':
            visited[d] = visited[num] + 'D'
            q.append(d)

        # S
        s = num - 1
        if s == -1:
            s = 9999
        if visited[s] == 'x':
            visited[s] = visited[num] + 'S'
            q.append(s)

        # L
        if len(str(num)) == 4:  # 1000, 1001 과 같은 경우도 커버
            l = (num - (num // 1000 * 1000)) * 10 + num // 1000
        else:
            l = num * 10
        if visited[l] == 'x':
            visited[l] = visited[num] + 'L'
            q.append(l)

        # R
        r = num // 10 + num % 10 * 1000  # 1000, 123과 같은 경우도 커버
        if visited[r] == 'x':
            visited[r] = visited[num] + 'R'
            q.append(r)

