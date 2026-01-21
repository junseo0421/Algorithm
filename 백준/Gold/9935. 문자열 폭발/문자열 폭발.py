import sys
input = sys.stdin.readline

string = input().rstrip()
explode = input().rstrip()

n = len(explode)

stack = []

for i in string:
    stack.append(i)

    if len(stack) >= n:
        if stack[-1] == explode[-1]:
            for j in range(n-1):
                if not stack[-2-j] == explode[-2-j]:
                    break
            else:
                for _ in range(n):
                    stack.pop()

if stack:
    sys.stdout.write("".join(stack))
else:
    sys.stdout.write('FRULA')