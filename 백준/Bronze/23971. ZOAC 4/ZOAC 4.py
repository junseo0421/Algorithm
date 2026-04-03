import sys
input = sys.stdin.readline

import math

R, C, N, M = map(int, input().split())

r_num = math.ceil(R / (N + 1))
c_num = math.ceil(C / (M + 1))

sys.stdout.write(str(r_num * c_num))