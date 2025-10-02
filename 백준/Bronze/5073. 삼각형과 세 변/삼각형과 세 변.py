import sys

while True:
    num_list = sorted(list(map(int, sys.stdin.readline().split())))

    if sum(num_list) == 0:
        break

    length = len(set(num_list))

    if sum(num_list[:2]) <= num_list[-1]:
        print("Invalid")
    elif length == 1:
        print("Equilateral")
    elif length == 2:
        print("Isosceles")
    else:
        print("Scalene")
