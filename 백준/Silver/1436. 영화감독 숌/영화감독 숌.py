import sys

n = int(sys.stdin.readline())
result = 666
cnt = 0

while True:
    if '666' in str(result):
        cnt += 1

    if cnt == n:
        print(result)
        break

    result += 1
    