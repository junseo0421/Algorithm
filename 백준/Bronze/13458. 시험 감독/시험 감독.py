import sys
input = sys.stdin.readline

import math

N = int(input())
A_lst = list(map(int, input().split()))
B, C = map(int, input().split())

result = N

for i in range(N):
    num = A_lst[i]

    num -= B

    if num <= 0:
        continue
    else:
        result += math.ceil(num / C)

sys.stdout.write(str(result))