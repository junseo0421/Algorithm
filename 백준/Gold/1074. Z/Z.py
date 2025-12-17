import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

ans = 0

while N >= 1:
    square_length = 2 ** (N-1)

    if r < square_length and c < square_length:  # 1사분면
        pass
    elif r < square_length and c >= square_length:  # 2사분면
        ans += square_length * square_length * 1
        c -= square_length
    elif r >= square_length and c < square_length:  # 3사분면
        ans += square_length * square_length * 2
        r -= square_length
    else:  # 4사분면
        ans += square_length * square_length * 3
        r -= square_length
        c -= square_length

    N -= 1

sys.stdout.write(str(ans))
