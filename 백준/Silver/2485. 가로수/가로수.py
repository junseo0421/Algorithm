import sys
import math

length = int(sys.stdin.readline())
diff = set()

first = int(sys.stdin.readline())
first_store = first

for _ in range(length-1):
    n = int(sys.stdin.readline())
    diff.add(n - first)
    first = n

list_diff = list(diff)
result = list_diff[0]

for i in range(1, len(list_diff)):
    result = math.gcd(result, list_diff[i])

print((n - first_store) // result - length + 1)
