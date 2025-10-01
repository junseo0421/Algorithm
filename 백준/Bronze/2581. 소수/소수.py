import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
prime_list = []

for i in range(M, N+1):
    if i < 2:
        continue
    elif i == 2:
        prime_list.append(i)
        continue
    elif i % 2 == 0:
        continue

    is_prime = True
    for j in range(3, int(i**0.5) + 1, 2):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(i)

if prime_list:
    print(sum(prime_list))
    print(min(prime_list))
else:
    print("-1")
