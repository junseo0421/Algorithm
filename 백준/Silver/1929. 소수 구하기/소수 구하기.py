import sys
import math

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return n == 2
    elif n % 3 == 0:
        return n == 3
    f = 5
    r = math.isqrt(n)
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True


m, n = map(int, sys.stdin.readline().split())

for i in range(m, n+1):
    if is_prime(i):
        print(i)
