import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_dict = {}

for idx, i in enumerate(sorted(set(num_list))):
    num_dict[i] = idx

print(' '.join(str(num_dict[j]) for j in num_list))
