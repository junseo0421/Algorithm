import sys
input = sys.stdin.readline

def main():
    SIZE = 9

    sudoku = [list(map(int, input().split())) for _ in range(SIZE)]
    black_coor = [(i, j) for i in range(SIZE) for j in range(SIZE) if sudoku[i][j] == 0]  # 빈 칸의 좌표

    def check(y, x, check_num):
        BOX_SIZE = 3

        for i in range(SIZE):
            if check_num == sudoku[i][x] or check_num == sudoku[y][i]:
                return False

        for i in range(BOX_SIZE):
            for j in range(BOX_SIZE):
                if sudoku[y // BOX_SIZE * BOX_SIZE + i][x // BOX_SIZE * BOX_SIZE + j] == check_num:
                    return False

        return True

    def dfs(n):
        if len(black_coor) == n:
            for nums in sudoku:
                print(' '.join(map(str, nums)))
            exit()

        for check_num in range(1, SIZE+1):
            y, x = black_coor[n]

            if check(y, x, check_num):
                sudoku[y][x] = check_num
                dfs(n+1)
                sudoku[y][x] = 0

    dfs(0)

main()
