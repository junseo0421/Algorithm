import sys
input = sys.stdin.readline

N, score, P = map(int, input().split())

if N == 0:
    print(1)
    exit()

score_lst = list(map(int, input().split()))

same = 0
idx = -1

for i in range(N):
    if idx == -1:
        if score_lst[i] <= score:
            idx = i + 1

    if score_lst[i] == score:
        same += 1
        
    if same >= 1 and score_lst[i] != score:
        break

# 가장 작은 경우
if idx == -1:
    if N == P:
        print(-1)
    else:
        print(N+1)

    exit()

if idx + same > P:
    print(-1)
else:
    print(idx)