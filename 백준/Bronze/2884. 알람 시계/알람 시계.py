A, B = map(int, input().split())

if (A > 0) and B < 45:
    A -= 1
    B = B - 45 + 60
elif (A == 0) and B < 45:
    A = A - 1 + 24
    B = B - 45 + 60
else:
    B -= 45

print(A, B)