import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

left = 0
max_len = 0
fruit_cnt = {}

for i in range(N):
    fruit = lst[i]

    if fruit in fruit_cnt:
        fruit_cnt[fruit] += 1
    else:
        fruit_cnt[fruit] = 1

    while len(fruit_cnt) > 2:
        fruit_remove = lst[left]

        fruit_cnt[fruit_remove] -= 1

        if fruit_cnt[fruit_remove] == 0:
            del fruit_cnt[fruit_remove]

        left += 1

    max_len = max(max_len, i-left+1)

sys.stdout.write(str(max_len))
