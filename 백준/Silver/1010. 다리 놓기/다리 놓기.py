import sys
from math import comb
input = sys.stdin.readline


def main():
    t = int(input())
    result = []

    for _ in range(t):
        west, east = map(int, input().split())

        result.append(str(comb(east, west)))

    sys.stdout.write("\n".join(result))

main()
