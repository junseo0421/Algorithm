import sys
from collections import deque

input = sys.stdin.readline


def main():
    _ = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    _ = int(input())
    c = list(map(int, input().split()))

    q = deque()
    result = []

    for is_que, num in zip(a, b):
        if not is_que:
            q.append(num)

    for i in c:
        q.appendleft(i)
        result.append(str(q.pop()))

    sys.stdout.write(" ".join(result))

main()
