import sys

num_list = []

while True:
    try:
        num_list.append(int(sys.stdin.readline()))
    except:
        break

num_max = max(num_list)

print(num_max)
print(num_list.index(num_max) + 1)
