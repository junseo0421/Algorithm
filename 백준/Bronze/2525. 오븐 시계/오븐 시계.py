A, B = map(int, input().split())
N = int(input())

B += N

if B >= 60:
    A += B // 60
    B = B % 60

if A >= 24:
    A = A % 24

print(A, B)
