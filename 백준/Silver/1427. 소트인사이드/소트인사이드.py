import sys

n = sorted(list(sys.stdin.readline().rstrip()), reverse=True)

print(''.join(i for i in n))
