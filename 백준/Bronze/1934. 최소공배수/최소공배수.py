import sys
import math

t = int(sys.stdin.readline())

result = []

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())

    result.append(math.lcm(a, b))

sys.stdout.write('\n'.join(map(str, result)))
