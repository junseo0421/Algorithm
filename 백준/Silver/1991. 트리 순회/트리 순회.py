import sys
input = sys.stdin.readline

n = int(input())

graph = {}

for _ in range(n):
    name, l, r = input().split()
    graph[name] = (l, r)  # 튜플 사용


result_pre, result_in, result_post = [], [], []

def dfs(node):
    left, right = graph[node]
    result_pre.append(node)

    if left != '.':
        dfs(left)
    result_in.append(node)

    if right != '.':
        dfs(right)
    result_post.append(node)

dfs('A')

sys.stdout.write(''.join(result_pre) + '\n')
sys.stdout.write(''.join(result_in) + '\n')
sys.stdout.write(''.join(result_post))