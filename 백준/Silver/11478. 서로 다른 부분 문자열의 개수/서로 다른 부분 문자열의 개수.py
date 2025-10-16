import sys

s = sys.stdin.readline().rstrip()
counts = {}

for i in range(2, len(s)): 
    for j in range(len(s) - i + 1):
        part = s[j:j+i]
        counts[part] = counts.get(part, 0) + 1

print(len(counts.keys()) + len(set(s)) + 1)
