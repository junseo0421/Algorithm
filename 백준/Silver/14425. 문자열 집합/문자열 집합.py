import sys

n, m = map(int, sys.stdin.readline().split())
set_list = [sys.stdin.readline().rstrip() for _ in range(n)]

set_dict = {i: 1 for i in set_list}

total = 0

for _ in range(m):
    if sys.stdin.readline().rstrip() in set_dict:
        total += 1

print(total)
