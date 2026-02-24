import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(n)]

for i in range(1, m+1):
    dot1, dot2 = map(int, input().split())

    if find_parent(dot1) != find_parent(dot2):
        union_parent(dot1, dot2)
    else:
        sys.stdout.write(str(i))
        exit()

sys.stdout.write('0')