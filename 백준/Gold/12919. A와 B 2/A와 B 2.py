import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

def backtracking(string):
    # 종료 조건
    if len(string) == len(S):
        if string == S:
            print(1)
            exit()
        return

    if string[-1] == 'A':
        backtracking(string[:-1])

    if string[0] == 'B':
        backtracking(string[1:][::-1])


backtracking(T)
print(0)