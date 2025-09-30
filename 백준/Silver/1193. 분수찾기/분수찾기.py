import sys

N = int(sys.stdin.readline())
line = 1

while N > line:
    N -= line
    line += 1

if line % 2 == 1:
    a = line - N + 1
    b = N
else:
    a = N
    b = line - N + 1

print(f"{a}/{b}")
