import sys
input = sys.stdin.readline

# 분리된 마을 안에서, 두 집 사이에 경로가 항상 존재하게 하면서 유지비의 합을 최소로

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())

edges = []
parent = [i for i in range(N+1)]


for _ in range(M):
    A, B, cost = map(int, input().split())
    edges.append((cost, A, B))

edges.sort()

i = 0
used_edge = 0
result = 0
while used_edge < N - 2:
    c, a, b = edges[i]

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += c
        used_edge += 1

    i += 1

sys.stdout.write(str(result))