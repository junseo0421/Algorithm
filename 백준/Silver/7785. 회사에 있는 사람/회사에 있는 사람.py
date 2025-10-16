import sys

n = int(sys.stdin.readline())

check_list = set()

for _ in range(n):
    a, b = sys.stdin.readline().split()

    if b == 'enter':
        check_list.add(a)
    else:
        check_list.discard(a)

print("\n".join(sorted(check_list, reverse=True)))
