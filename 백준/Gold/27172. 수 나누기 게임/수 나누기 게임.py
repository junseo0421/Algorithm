import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

MAX = max(cards)
present = [False] * (MAX + 1)
ans = [0] * (MAX + 1)

for card in cards:
    present[card] = True

for i in range(N):
    card = cards[i]
    k = 2

    while k * card <= MAX:
        if present[k * card]:
            ans[card] += 1
            ans[k * card] -= 1

        k += 1

for i in cards:
    sys.stdout.write(str(ans[i]) + ' ')