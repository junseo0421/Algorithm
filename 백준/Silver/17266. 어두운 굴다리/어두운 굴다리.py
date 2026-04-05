import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lights = list(map(int, input().split()))

diff = 0

prev = lights[0]

if M == 1:
    pass
else:
    for x in lights[1:]:
        diff = max(diff, x - prev)
        prev = x

first, last = lights[0], N - lights[-1]


print(max(-(-diff // 2), first, last))