import sys
import math

a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())

lcm = math.lcm(b1, b2)

result = a1 * (lcm // b1) + a2 * (lcm // b2)

gcd = math.gcd(result, lcm)

print(result // gcd, lcm // gcd)
