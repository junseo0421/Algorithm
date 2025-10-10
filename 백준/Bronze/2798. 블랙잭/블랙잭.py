import sys

a1, a2 = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

max_num = 0

for i in range(a1):
    for j in range(i+1, a1):
        for z in range(j+1, a1):
            total = num_list[i] + num_list[j] + num_list[z]

            if (total <= a2) and (total > max_num):
                max_num = total

print(max_num)
