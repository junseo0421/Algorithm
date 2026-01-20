import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

tree_lst = []

while True:
    a = input().strip()
    if not a:
        break

    tree_lst.append(int(a))

def index_split(start, end):
    # 종료 조건
    if start > end:
        return

    root = tree_lst[start]
    spl = end + 1

    for i in range(start+1, end + 1):
        if root < tree_lst[i]:
            spl = i
            break

    index_split(start+1, spl-1)
    index_split(spl, end)
    sys.stdout.write(str(root) + "\n")

index_split(0, len(tree_lst)-1)