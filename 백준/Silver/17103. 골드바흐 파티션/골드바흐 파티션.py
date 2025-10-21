import sys
import math

result = []

nums = list(map(int, sys.stdin.read().split()))[1:]

N = max(nums)
length = len(nums)

is_comp = [False] * (N+1)

if N >= 0:
    is_comp[0] = True
if N >= 1:
    is_comp[1] = True

limit = math.isqrt(N)

for p in range(2, limit+1):
    if not is_comp[p]:
        start = p*p
        step = p
        is_comp[start:N+1:step] = [True] * ((N - start) // step + 1)

for i in nums:
    total = 0
    for j in range(1, i//2):
        if not (is_comp[j] or is_comp[i-j]):
            total += 1
    if not is_comp[i//2]:
        total += 1
    result.append(str(total))

sys.stdout.write("\n".join(result))
