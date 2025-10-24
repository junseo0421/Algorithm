import sys
input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    up, down = 1, 1

    for i in range(n-k+1, n+1):
        up *= i

    for j in range(2, k+1):
        down *= j

    sys.stdout.write(str(up // down))


main()
