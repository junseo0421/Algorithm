import sys
input = sys.stdin.readline


def main():
    _ = int(input())

    num_list = list(map(int, input().split()))
    sys.stdout.write(str(max(num_list) * min(num_list)))


main()
