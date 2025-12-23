import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

visited = [0] * (N+1)

result = []

def back():
    prev = None
    if len(result) == M:
        sys.stdout.write(' '.join(map(str, result)) + '\n')
        return

    for i in range(N):  # idx
        if visited[i] == 0 and prev != lst[i]:
            visited[i] = 1
            result.append(lst[i])
            prev = lst[i]
            back()
            result.pop()
            visited[i] = 0

back()