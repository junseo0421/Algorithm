import sys

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    while not is_prime(num):
        num += 1
    print(num)
