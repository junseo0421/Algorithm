import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num_lst = list(map(int, input().split()))

INF = float('inf')
ans = INF

cur = 0
left = 0
right = 0

while True:
    if right == N and cur < S:
        break

    if cur < S:
        cur += num_lst[right]  # 우측 확장
        right += 1
    else:
        ans = min(ans, right - left)
        cur -= num_lst[left]
        left += 1

if ans == INF:
    sys.stdout.write('0')
else:
    sys.stdout.write(str(ans))
