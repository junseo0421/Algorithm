import sys

N = int(sys.stdin.readline())

x_list = []
y_list = []

for i in range(N):
    X, Y = map(int, sys.stdin.readline().split())
    x_list.append(X)
    y_list.append(Y)
    
print((max(x_list) - min(x_list)) * (max(y_list) - min(y_list)))
