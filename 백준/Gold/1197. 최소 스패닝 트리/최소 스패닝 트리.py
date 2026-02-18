import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# Kruskal 알고리즘

# 그리디 알고리즘의 일종. 사이클이 만들어지면 안되고, 간선은 n-1 개만 존재해야함.

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # 경로 압축
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 두 집합을 합침 (연결)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())

parent = [0] * (V + 1)
edges = []

for i in range(1, V+1):  # parent 배열 초기화
    parent[i] = i

for _ in range(E):
    A, B, weight = map(int, input().split())
    edges.append((weight, A, B))

edges.sort()  # 가중치를 기준으로 오름차순으로 정렬

result = 0

for edge in edges:
    w, a, b = edge

    # 같은 집합에 포함이 안 됐을 경우 (사이클이 안 만들어지는 경우) 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += w

sys.stdout.write(str(result))