import sys
input = sys.stdin.readline

M = int(input())

mod = 1000000007

# 역원에서의 분할 정복 함수 구현, 각 재귀에서 mod 넣어줘야함
def recursion_power(x, n):
    if n == 1:
        return x

    y = recursion_power(x, n // 2) % mod

    if n % 2 == 0:
        return (y * y) % mod
    else:
        return (((y * y) % mod) * (x % mod)) % mod

# a * b^(-1) 구현 (S_i / N_i)
N, S = map(int, input().split())
expected = (S % mod) * (recursion_power(N, mod-2) % mod) % mod

# 모든 주사위들 더하고 mod (분배법칙 사용?)
for _ in range(M-1):
    N, S = map(int, input().split())
    expected = (expected + ((S % mod) * (recursion_power(N, mod-2) % mod) % mod)) % mod

sys.stdout.write(str(expected))