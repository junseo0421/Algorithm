import sys

N = int(sys.stdin.readline())
total = N

for i in range(N):
    A = sys.stdin.readline().rstrip()
    A_list = []
    re = ""

    for j in A:
        if j != re:
            if j in A_list:
                total -= 1
                break
            A_list.append(j)
        re = j

print(total)