import sys
from collections import deque

input = sys.stdin.readline


def main():
    n = int(input())
    queue = deque()
    result = []

    for _ in range(n):
        inst = input().rstrip()

        if 'push' in inst:
            _, a = inst.split()
            queue.append(int(a))
        elif inst == 'pop':
            if queue:
                result.append(queue[0])
                queue.popleft()
            else:
                result.append(-1)
        elif inst == 'size':
            result.append(len(queue))
        elif inst == 'empty':
            result.append(0 if queue else 1)
        elif inst == 'front':
            result.append(queue[0] if queue else -1)
        elif inst == 'back':
            result.append(queue[-1] if queue else -1)

    sys.stdout.write("\n".join(map(str, result)))


main()
