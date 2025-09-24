import sys

num_list = []

for _ in range(10):
    num_list.append(int(sys.stdin.readline()))

remain = [i % 42 for i in num_list]

print(len(set(remain)))
