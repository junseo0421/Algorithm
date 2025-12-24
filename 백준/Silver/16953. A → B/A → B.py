import sys
input = sys.stdin.readline

from collections import deque

a, b = map(int, input().split())

def bfs(n, d):
    q = deque()
    q.append([n, d])

    is_exist = False


    while q:
        num, depth = q.popleft()

        if num == b:
            sys.stdout.write(str(depth + 1))
            is_exist = True
            break

        for i in (num*2, num*10+1):
            if i <= b:
                q.append([i, depth+1])

    if not is_exist:
        sys.stdout.write('-1')

bfs(a, 0)