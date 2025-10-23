import sys
from collections import deque

input = sys.stdin.readline


def main():
    n = int(input())

    que = deque()
    result = []
    r = result.append

    for _ in range(n):
        order = input().rstrip()
        if order.startswith('1'):
            _, num = order.split()
            que.appendleft(int(num))
        elif order.startswith('2'):
            _, num = order.split()
            que.append(int(num))
        elif order == '3':
            if que:
                r(que.popleft())
            else:
                r(-1)
        elif order == '4':
            if que:
                r(que.pop())
            else:
                r(-1)
        elif order == '5':
            r(len(que))
        elif order == '6':
            if que:
                r(0)
            else:
                r(1)
        elif order == '7':
            if que:
                r(que[0])
            else:
                r(-1)
        elif order == '8':
            if que:
                r(que[-1])
            else:
                r(-1)
    
    sys.stdout.write("\n".join(map(str, result)))

main()
