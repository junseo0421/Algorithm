import sys

n = int(sys.stdin.readline())

sub = len(str(n)) * 9

for i in range(max(0, n - sub), n):
    sum = 0
    for j in str(i):
        sum += int(j)

    if (i+sum) == n:
        print(i)
        break
else:
    print(0)
