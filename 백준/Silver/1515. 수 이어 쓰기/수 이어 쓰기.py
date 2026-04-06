import sys
input = sys.stdin.readline

numbers = input().rstrip()

N = len(numbers)

p = 0
i = 1

is_finish = 0

while True:
    for n in str(i):
        if numbers[p] == n:
            p += 1

            if p >= N:
                is_finish = 1
                break

    if is_finish:
        print(i)
        break

    i += 1
