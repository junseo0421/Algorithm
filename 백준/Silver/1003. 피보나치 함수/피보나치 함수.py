import sys
input = sys.stdin.readline

# n은 최대 40이므로 0~40까지 미리 계산
MAX_N = 40
zero = [0] * (MAX_N + 1)
one = [0] * (MAX_N + 1)

# 초기값: fib(0) 호출 시 (1, 0), fib(1) 호출 시 (0, 1)
zero[0], one[0] = 1, 0
zero[1], one[1] = 0, 1

for i in range(2, MAX_N + 1):
    zero[i] = zero[i-1] + zero[i-2]
    one[i] = one[i-1] + one[i-2]

N = int(input())

for _ in range(N):
    num = int(input())
    print(zero[num], one[num])