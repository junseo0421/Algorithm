import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visits = list(map(int, input().split()))

right = X
current_sum = sum(visits[:X])
max_sum = current_sum
number = 1

for _ in range(N - X):
    current_sum = current_sum - visits[right - X] + visits[right]

    if max_sum == current_sum:
        number += 1
    elif max_sum < current_sum:
        number = 1
        max_sum = current_sum

    right += 1

if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(number)