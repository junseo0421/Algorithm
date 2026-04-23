import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a
        
        
V, E = map(int, input().split())

edges = []

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()

parent = []

for i in range(V + 1):
    parent.append(i)

ans = 0
used_edges = 0

for cost, start, finish in edges:
    if find_parent(start) != find_parent(finish):
        ans += cost
        union(start, finish)
        used_edges += 1

        if used_edges == V - 1:
            break

print(ans)