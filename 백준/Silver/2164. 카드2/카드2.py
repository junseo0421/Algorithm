import sys
from collections import deque

input = sys.stdin.readline


def main():
    n = int(input())
    que = deque()

    for i in range(1, n+1):
        que.append(i)

    for count in range(1, n):
        que.popleft()
        que.append(que.popleft())
        
    sys.stdout.write(str(que[0]))

main()
