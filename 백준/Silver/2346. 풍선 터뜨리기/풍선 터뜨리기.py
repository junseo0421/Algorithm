import sys
from collections import deque

input = sys.stdin.readline


def main():
    n = int(input())
    step = list(map(int, input().split()))

    q = deque()

    for idx, i in enumerate(step):
        q.append((idx+1, i))

    result = []

    for i in range(n-1):
        t = q.popleft()
        order, step = t[0], t[1]
        result.append(order)

        if step > 0:
            q.rotate(-(step-1))
        else:
            q.rotate(-step)

    result.append(q.popleft()[0])

    sys.stdout.write(' '.join(map(str, result)))


main()
