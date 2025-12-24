import sys
input = sys.stdin.readline

n = int(input())

h_lst = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    h_lst[i][0] += min(h_lst[i-1][1], h_lst[i-1][2])
    h_lst[i][1] += min(h_lst[i-1][0], h_lst[i-1][2])
    h_lst[i][2] += min(h_lst[i-1][0], h_lst[i-1][1])

sys.stdout.write(str(min(h_lst[n-1][0], h_lst[n-1][1], h_lst[n-1][2])))
