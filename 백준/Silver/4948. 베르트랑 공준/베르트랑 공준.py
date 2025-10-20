import sys
import math

result = []

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    n_2 = 2 * n

    is_comp = [False] * (n_2 + 1)

    if n_2 >= 0:
        is_comp[0] = True
    if n_2 >= 1:
        is_comp[1] = True

    limit = math.isqrt(n_2)

    for p in range(2, limit+1):
        if not is_comp[p]:
            start = p * p
            step = p
            is_comp[start:n_2+1:step] = [True] * ((n_2 - start) // step + 1)

    total = 0

    for x in range(n+1, n_2 + 1):
        if not is_comp[x]:
            total += 1

    result.append(str(total))

sys.stdout.write('\n'.join(result))
