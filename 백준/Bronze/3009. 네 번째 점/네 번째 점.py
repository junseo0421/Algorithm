import sys

x_list = []
y_list = []

for _ in range(3):
    X, Y = map(int, sys.stdin.readline().split())

    if not X in x_list:
        x_list.append(X)
    else:
        x_list.remove(X)
        
    if not Y in y_list:
        y_list.append(Y)
    else:
        y_list.remove(Y)
    
print(x_list[0], y_list[0])
    
