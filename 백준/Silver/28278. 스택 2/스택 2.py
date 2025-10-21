import sys

def command(input, stack):
    if input[0] == 1:
        stack.append(input[1])
    elif input[0] == 2:
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif input[0] == 3:
        print(len(stack))
    elif input[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)

input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    order = list(map(int, input().split()))
    command(order, stack)
