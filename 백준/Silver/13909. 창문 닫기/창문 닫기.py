import sys

n = int(sys.stdin.readline())
i = 1

while True:
    if i*i > n:
        break

    i += 1

print(i-1)