import sys

num_list = []

for _ in range(3):
    num_list.append(int(sys.stdin.readline()))

length = len(set(num_list))

if sum(num_list) != 180:
    print("Error")
elif length == 1:
    print("Equilateral")
elif length == 2:
    print("Isosceles")
else:
    print("Scalene")
