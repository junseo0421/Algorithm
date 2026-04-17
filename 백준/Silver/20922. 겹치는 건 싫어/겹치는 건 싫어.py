import sys
input = sys.stdin.readline

# 2개의 포인터로 관리.

ans = 0

N, K = map(int, input().split())
num_lst = list(map(int, input().split()))

left = right = 0
cnt = [0] * 100001

while right < N:
    cnt[num_lst[right]] += 1

    while cnt[num_lst[right]] > K:
        cnt[num_lst[left]] -= 1
        left += 1

    right += 1
    ans = max(right - left, ans)

print(ans)