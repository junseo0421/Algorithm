import sys
input = sys.stdin.readline

# 팰린드롬: 앞으로 읽으나 뒤로 읽으나 같은 단어, 문장, 숫자, 문자열

# 길이 기준으로 2D 를 채우거나 dp[l][r] 2d matrix 생성

N = int(input())
num_lst = list(map(int, input().split()))
M = int(input())

dp = [[0] * N for _ in range(N)]  # 0이면 팰린드롬 아님, 1이면 맞음

for i in range(N):
    l, r = 1, 1
    while True:
        if i - l < 0 or i + r >= N:
            break

        if num_lst[i - l] == num_lst[i + r]:
            dp[i - l][i + r] = 1
            l += 1
            r += 1
        else:
            break

for i in range(N):
    l, r = 0, 1
    while True:
        if i - l < 0 or i + r >= N:
            break

        if num_lst[i - l] == num_lst[i + r]:
            dp[i - l][i + r] = 1
            l += 1
            r += 1
        else:
            break


for _ in range(M):
    S, E = map(int, input().split())

    if S == E:
        sys.stdout.write('1\n')
    else:
        sys.stdout.write(str(dp[S-1][E-1]) + '\n')