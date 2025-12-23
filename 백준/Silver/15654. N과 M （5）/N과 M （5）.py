import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_lst = sorted(list(map(int, input().split())))

result = []

def back():
    if len(result) == M:
        sys.stdout.write(' '.join(map(str, result)) + '\n')
        return

    for i in range(N):
        if num_lst[i] not in result:
            result.append(num_lst[i])
            back()
            result.pop()

back()