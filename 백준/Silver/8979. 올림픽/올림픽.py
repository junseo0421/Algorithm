import sys
input = sys.stdin.readline

N, K = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]
lst = sorted(lst, key = lambda x: (x[1], x[2], x[3]), reverse=True)

if K == lst[0][0]:
    print(1)
    exit()

lst[0].append(1)

prev = lst[0]

for i in range(1, N):
    if prev[1:4] == lst[i][1:4]:
        lst[i].append(prev[4])
        prev = lst[i]
    else:
        lst[i].append(i+1)
        prev = lst[i]

    if K == lst[i][0]:
        print(lst[i][4])
        break
