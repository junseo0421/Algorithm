import sys

x, y, w, h = map(int, sys.stdin.readline().split())

if w - x >= x:
    axis_x = x
else:
    axis_x = w - x

if h - y >= y:
    axis_y = y
else:
    axis_y = h - y

print(min(axis_x, axis_y))
