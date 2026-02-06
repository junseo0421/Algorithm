import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

result = []

A_sort = sorted(A)
B_sort = sorted(B)

while True:
    if len(A_sort) == 0 or len(B_sort) == 0:
        break

    if A_sort[-1] == B_sort[-1]:
        same = A_sort[-1]
        result.append(same)

        A_idx = A.index(same)
        B_idx = B.index(same)

        if A_idx == N-1 or B_idx == M-1:
            break

        A = A[A_idx + 1:]
        B = B[B_idx + 1:]

        A_sort = sorted(A)
        B_sort = sorted(B)

    elif A_sort[-1] > B_sort[-1]:
        A_sort.pop()
    else:
        B_sort.pop()

length = len(result)
sys.stdout.write(str(length))
if length:
    sys.stdout.write("\n")
    sys.stdout.write(" ".join(map(str, result)))