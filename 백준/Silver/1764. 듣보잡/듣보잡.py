import sys

n, m = map(int, sys.stdin.readline().split())

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(sys.stdin.readline().rstrip())
    
for _ in range(m):
    m_set.add(sys.stdin.readline().rstrip())
    
inter_set = n_set.intersection(m_set)

print(len(inter_set))
sys.stdout.write('\n'.join(sorted(inter_set)))
