import sys
input = sys.stdin.readline


def main():
    n = int(input())

    if n > 1:
        print(n * (n-1))
    else:
        print(0)

main()
