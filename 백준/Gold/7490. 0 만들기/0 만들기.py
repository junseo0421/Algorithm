import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

T = int(input())

def dfs(num, expr):
    # 완성된 식 검사
    if num == N:
        total = 0
        value = 0  # 자릿수 검사 용
        sign = 1  # 부호
        new_expr = expr.replace(" ", "")  # 공백 없애기

        for ch in new_expr:
            if ch.isdigit():
                value = value * 10 + int(ch)
            else:
                total += value * sign
                value = 0

                if ch == '+':
                    sign = 1
                else:
                    sign = -1

        total += value * sign

        if total == 0:
            ans.append(expr)
        return

    next_num = num + 1

    dfs(next_num, expr + " " + str(next_num))
    dfs(next_num, expr + "+" + str(next_num))
    dfs(next_num, expr + "-" + str(next_num))

for _ in range(T):
    N = int(input())

    ans = []
    dfs(1, "1")

    for i in ans:
        print(i)

    print()