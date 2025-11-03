import sys
input = sys.stdin.readline

def main():
    def blank_center(arr, r0, r1, c0, c1):
        size = r1 - r0 + 1
        step = size // 3

        for i in range(r0+step, r0+step*2):
            arr[i][c0+step:c0+step*2] = [" "] * step

    def split_str(arr, r0, r1, c0, c1):
        size = r1 - r0 + 1
        
        if size < 3:
            return
        
        step = size // 3

        blank_center(arr, r0, r1, c0, c1)

        for dr in (0, step, step * 2):
            for dc in (0, step, step * 2):
                if dr == step and dc == step:
                    continue
                nr0, nr1 = r0 + dr, r0 + dr + step - 1
                nc0, nc1 = c0 + dc, c0 + dc + step - 1

                split_str(arr, nr0, nr1, nc0, nc1)

    n = int(input())

    arr_2d = [['*'] * n for _ in range(n)]

    split_str(arr_2d, 0, n-1, 0, n-1)

    for arr in arr_2d:
        print(''.join(arr))

main()

