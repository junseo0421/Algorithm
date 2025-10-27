import sys
input = sys.stdin.readline


def main():
    n = int(input())

    name_set = set()
    name_set.add('ChongChong')
    
    for _ in range(n):
        a, b = input().split()
        if a in name_set:
            name_set.add(b)
        elif b in name_set:
            name_set.add(a)

    sys.stdout.write(str(len(name_set)))

main()
