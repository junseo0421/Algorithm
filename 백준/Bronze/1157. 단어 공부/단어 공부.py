import sys

A = sys.stdin.readline().rstrip().upper()

alpha_list = list(set(A))
num_list = [0] * len(alpha_list)

for i in A:
    num_list[alpha_list.index(i)] += 1

if num_list.count(max(num_list)) != 1:
    print("?")
else:
    print(alpha_list[num_list.index(max(num_list))])