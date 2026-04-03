import sys
input = sys.stdin.readline

P = int(input())

for _ in range(P):
    result = 0

    case = list(map(int, input().split()))
    test_number, children = case[0], case[1:]

    for i in range(1, 20):
        for j in range(i):
            if children[j] > children[i]:
                result += 1

    print(test_number, result)