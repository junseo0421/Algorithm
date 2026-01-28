import sys
input = sys.stdin.readline

N = int(input())
num_lst = list(map(int, input().split()))

dp_inc, dp_dec = [0] * N, [0] * N
dp_inc[0] = 1
dp_dec[-1] = 1


for i in range(1, N):
    max_inc = 0

    for inc in range(i):
        if num_lst[i] > num_lst[inc]:
            max_inc = max(max_inc, dp_inc[inc])

    if max_inc:
        dp_inc[i] = max_inc + 1
    else:
        dp_inc[i] = 1


for i in range(N-2, -1, -1):
    max_dec = 0

    for dec in range(N-1, i, -1):
        if num_lst[i] > num_lst[dec]:
            max_dec = max(max_dec, dp_dec[dec])

    if max_dec:
        dp_dec[i] = max_dec + 1
    else:
        dp_dec[i] = 1

result = 0

for i in range(N):
    result = max(result, dp_inc[i] + dp_dec[i] - 1)

sys.stdout.write(str(result))