total = int(input())
N = int(input())

buy = 0

for i in range(N):
    A, B = map(int, input().split())
    buy += A * B

if buy == total:
    print("Yes")
else:
    print("No")
