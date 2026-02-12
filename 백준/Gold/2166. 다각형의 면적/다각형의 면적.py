import sys
input = sys.stdin.readline

N = int(input())

x_lst = []
y_lst = []

for _ in range(N):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

area = 0

for i in range(N-1):
    area += (x_lst[i] + x_lst[i+1]) * (y_lst[i] - y_lst[i+1])

area += (x_lst[N-1] + x_lst[0]) * (y_lst[N-1] - y_lst[0])

result = round(abs(area) / 2, 1)

sys.stdout.write(str(result))