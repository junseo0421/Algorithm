import sys
input = sys.stdin.readline

N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
    x, y = lst[i]

    rank = 1
    for j in range(N):
        a, b = lst[j]

        if x < a and y < b:
            rank += 1

    print(rank, end=' ')