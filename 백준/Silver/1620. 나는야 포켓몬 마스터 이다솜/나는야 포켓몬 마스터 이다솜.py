import sys

n, m = map(int, sys.stdin.readline().split())
po_dict = {}
po_dict_rev = {}

for i in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    po_dict[name] = str(i)
    po_dict_rev[str(i)] = name

for _ in range(m):
    question = sys.stdin.readline().rstrip()

    if question in po_dict:
        print(po_dict[question])
    else:
        print(po_dict_rev[question])
        