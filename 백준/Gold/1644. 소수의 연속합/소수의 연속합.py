import sys
input = sys.stdin.readline

N = int(input())

prime = [1 for _ in range(N+1)]

for i in range(2, int(N**(1/2)) + 1):
    if prime[i] == 0:
        continue

    k = 2

    while i * k <= N:
        prime[i * k] = 0
        k += 1

prime_lst = []

for i in range(2, N+1):
    if prime[i] == 1:
        prime_lst.append(i)

cur = left = right = 0

length = len(prime_lst)

ans = 0

while True:
    if right == length and cur < N:
        break
    if cur == N:
        ans += 1
        cur -= prime_lst[left]
        left += 1
    elif cur < N:
        cur += prime_lst[right]
        right += 1
    else:
        cur -= prime_lst[left]
        left += 1

sys.stdout.write(str(ans))