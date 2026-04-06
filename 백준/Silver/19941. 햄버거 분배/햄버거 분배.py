import sys
input = sys.stdin.readline

N, K = map(int, input().split())
string = list(input().rstrip())

result = 0

for i in range(N):
    if string[i] == 'P':
        is_find = 0

        for j in range(K, 0, -1):
            if i - j < 0:
                continue

            if string[i - j] == 'H':
                string[i - j] = 'E'
                result += 1
                is_find = 1
                break

        if is_find:
            continue

        for j in range(1, K + 1):
            if i + j >= N:
                break

            if string[i + j] == 'H':
                string[i + j] = 'E'
                result += 1
                break

print(result)