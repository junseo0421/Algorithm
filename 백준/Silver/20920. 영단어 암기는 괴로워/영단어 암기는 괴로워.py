import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())

    string_dict = {}

    for _ in range(n):
        string = input().rstrip()

        if len(string) < m:
            continue

        string_dict[string] = string_dict.get(string, 0) - 1

    dict2 = sorted(string_dict.items(), key=lambda x: (x[1], -len(x[0]), x[0]))

    for i in dict2:
        print(i[0])

main()
