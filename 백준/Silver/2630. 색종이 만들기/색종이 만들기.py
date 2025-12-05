import sys
input = sys.stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

def paper_split(y, x, n):
    color = paper[y][x]

    for r in range(y, y+n):
        for c in range(x, x+n):
            if color != paper[r][c]:
                m = n // 2
                paper_split(y, x, m)
                paper_split(y, x+m, m)
                paper_split(y+m, x, m)
                paper_split(y+m, x+m, m)
                return

    if color == 1:
        result[1] += 1
    else:
        result[0] += 1

result = [0, 0]

paper_split(0, 0, N)

print(result[0])
print(result[1])