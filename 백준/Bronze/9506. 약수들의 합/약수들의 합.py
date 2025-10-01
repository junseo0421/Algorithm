import sys

while True:
    N = int(sys.stdin.readline())

    if N == -1:
        break

    num_list = []

    for i in range(1, N//2 + 1):
        if N % i == 0:
            num_list.append(i)

    if sum(num_list) == N:
        num_list_str = ' '.join(map(str, num_list)).replace(" ", " + ")
        print(f"{N} = {num_list_str}")
    else:
        print(f"{N} is NOT perfect.")
