import sys
input = sys.stdin.readline


def main():
    n = int(input())
    total = 0
    string_dict = {}

    for _ in range(n):
        string = input().rstrip()

        if string == 'ENTER':
            string_dict.clear()
            continue

        if string in string_dict:
            continue
        else:
            string_dict[string] = 1
            total += 1

    sys.stdout.write(str(total))

main()
