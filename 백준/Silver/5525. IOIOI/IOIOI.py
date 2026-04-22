import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
string = input().rstrip()

i, ans, cnt = 0, 0, 0

while i < M - 2:
    if string[i:i+3] == 'IOI':
        cnt += 1
        if cnt >= N:
            ans += 1
        i += 2
    else:
        cnt = 0
        i += 1

print(ans)