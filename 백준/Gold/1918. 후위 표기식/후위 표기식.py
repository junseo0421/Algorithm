import sys
input = sys.stdin.readline

equation = input().rstrip()
priority = {'+': 1, '-': 1, '*': 2, '/': 2}
parent = {'(': 0, ')': 0}

stack = []
result = []

for i in equation:
    if (i not in priority) and (i not in parent):
        result.append(i)  # 알파벳은 바로 result로 push
        continue

    # stack 이 비어있으면 바로 push / 정상적인 수식이면 ')' 으로 시작하는 경우는 없을 것
    if not stack:
        stack.append(i)
        continue

    if i == '(':
        stack.append(i)
    elif i == ')':
        while True:
            o = stack.pop()

            if o == '(':
                break

            result.append(o)
    elif stack[-1] != '(':
        while priority[i] <= priority[stack[-1]]:  # stack의 top과 우선 순위가 같거나 높은 경우는 출력 후 본인 push
            result.append(stack.pop())
            if not stack:
                break
            if stack[-1] == '(':
                break
        stack.append(i)
    else:
        stack.append(i)

while stack:
    result.append(stack.pop())

sys.stdout.write("".join(map(str, result)))