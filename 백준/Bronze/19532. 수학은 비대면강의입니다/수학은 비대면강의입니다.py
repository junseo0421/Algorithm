import sys
import math

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

if a == 0:
    y = c // b
    x = (f - e * y) // d
elif d == 0:
    y = f // e
    x = (c - b * y) // a
else:
    lcm = math.lcm(abs(a), abs(d))

    eq1 = lcm // abs(a)
    eq2 = lcm // abs(d)

    b1, c1 = eq1 * b, eq1 * c
    e2, f2 = eq2 * e, eq2 * f

    if a*d > 0:
        be = b1 - e2
        cf = c1 - f2
    else:
        be = b1 + e2
        cf = c1 + f2

    y = cf // be
    x = (c - b * y) // a

print(x, y)
