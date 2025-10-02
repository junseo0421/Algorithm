import sys

num_list = sorted(list(map(int, sys.stdin.readline().split())))

if sum(num_list[:2]) <= num_list[-1]:
    num_list[-1] = sum(num_list[:2]) - 1

print(sum(num_list))
