import sys
from collections import deque

input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    result = []
    que = deque(range(1, n+1))

    for _ in range(n):
        que.rotate(-(k-1))
        result.append(que.popleft())

    sys.stdout.write("<" + ", ".join(map(str, result)) + ">")

main()
