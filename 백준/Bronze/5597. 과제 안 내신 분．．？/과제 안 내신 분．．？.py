import sys

num_list = [1]*30

for _ in range(28):
    num_list[int(sys.stdin.readline()) - 1] -= 1

for idx, i in enumerate(num_list):
    if i == 1:
        print(idx+1)
