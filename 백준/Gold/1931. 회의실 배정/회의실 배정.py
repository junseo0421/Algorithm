import sys
input = sys.stdin.readline

N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

lst = sorted(lst, key=lambda x: [x[1], x[0]])

endpoint = 0
cnt = 0

for start, end in lst:
    if start >= endpoint:
        cnt += 1
        endpoint = end

sys.stdout.write(str(cnt))