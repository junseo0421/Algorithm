import sys

num_list = []

for _ in range(5):
    num_list.append(int(sys.stdin.readline()))

print(sum(num_list) // len(num_list))
print(sorted(num_list)[2])
