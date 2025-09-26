import sys

A = sys.stdin.readline().rstrip()

alpha_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

total = 0

for i in alpha_list:
    if i in A:
        total += A.count(i)
        A = A.replace(i, " ")

print(total + len(A.replace(" ", "")))
