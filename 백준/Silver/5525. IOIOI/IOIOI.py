import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

string = 'IO' * N + 'I'

cnt = 0
string_len = 2*N+1

for i in range(M - string_len + 1):
    if string == S[i:i+string_len]:
        cnt += 1

sys.stdout.write(str(cnt))
