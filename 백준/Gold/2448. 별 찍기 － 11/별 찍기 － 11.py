import sys
input = sys.stdin.readline

N = int(input())

star = [list(' ' * (N * 2 - 1)) for _ in range(N)]

def draw(r, c, n):  # 가장 작은 삼각형의 맨 위 꼭짓점 좌표, 크기
    if n == 3:
        star[r][c] = '*'
        star[r+1][c-1], star[r+1][c+1] = '*', '*'
        for i in range(5):
            star[r+2][c-2+i] = '*'
        return
    else:
        draw(r, c, n // 2)
        draw(r + n // 2, c + n // 2, n // 2)
        draw(r + n // 2, c - n // 2, n // 2)

draw(0, N-1, N)

sys.stdout.write("\n".join("".join(row) for row in star))
