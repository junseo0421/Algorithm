import sys
input = sys.stdin.readline

M = int(input())

mod = 1000000007

expected = 0

for _ in range(M):
    N, S = map(int, input().split())
    expected = (expected + (S % mod) * pow(N, mod-2, mod)) % mod

sys.stdout.write(str(expected))