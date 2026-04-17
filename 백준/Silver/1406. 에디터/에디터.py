import sys
input = sys.stdin.readline

left = list(input().rstrip())  # 커서 왼쪽의 문자열 스택
right = []  # 커서 오른쪽의 문자열 스택

M = int(input())

for _ in range(M):
    command = list(input().split())

    if command[0] == 'L':
        if left:
            right.append(left.pop())

    elif command[0] == 'D':
        if right:
            left.append(right.pop())

    elif command[0] == 'B':
        if left:
            left.pop()

    else:
        left.append(command[1])

sys.stdout.write(''.join(left + right[::-1]))