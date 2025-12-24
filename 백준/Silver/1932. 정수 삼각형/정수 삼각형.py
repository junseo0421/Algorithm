import sys
input = sys.stdin.readline

n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):  # 행 고르기
    lst[i][0] += lst[i-1][0]

    for j in range(1, i):  # 중간에 있는 숫자, j = 1 ~ i-1
        # 8 1 0
        lst[i][j] += max(lst[i-1][j-1], lst[i-1][j])

    lst[i][i] += lst[i-1][i-1]  # 마지막 숫자
    
sys.stdout.write(str(max(lst[n-1])))
