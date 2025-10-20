import sys
import math

m, n = map(int, sys.stdin.readline().split())

is_comp = [False] * (n+1)

if n >= 0:
    is_comp[0] = True
if n >= 1:
    is_comp[1] = True

limit = math.isqrt(n)

for p in range(2, limit+1):
    if not is_comp[p]:
        start = p * p
        step = p
        is_comp[start:n+1:step] = [True] * ((n - start) // step + 1)

result = []
for x in range(m, n+1):
    if not is_comp[x]:
        result.append(str(x))

sys.stdout.write('\n'.join(result))
