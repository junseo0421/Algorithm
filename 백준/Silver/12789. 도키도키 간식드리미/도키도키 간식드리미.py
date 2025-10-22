import sys
input = sys.stdin.readline


def main():
    n = int(input())
    num_list = list(map(int, input().split()))
    stack = []
    order = 1

    for num in num_list:
        while stack and stack[-1] == order:
            stack.pop()
            order += 1

        if num == order:
            order += 1
        else:
            stack.append(num)

    while stack and stack[-1] == order:
        stack.pop()
        order += 1

    print("Nice" if order == n+1 else "Sad")


main()
