import sys

num_list = [1, 1, 2, 2, 2, 8]
input_list = list(map(int, sys.stdin.readline().split()))

total = []

for idx, i in enumerate(input_list):
    total.append(num_list[idx] - i)

print(*total)
