import sys
input = sys.stdin.readline

N = int(input())
budget = list(map(int, input().split()))
M = int(input())

t_budget = sum(budget)
m_budget = max(budget)

if t_budget <= M:
    print(m_budget)
    exit()

left = m_budget - (t_budget - M)
right = m_budget

while left <= right:
    summation = 0
    mid = (right + left) // 2

    for i in range(N):
        summation += min(budget[i], mid)

        if summation > M:
            break

    if summation > M:
        right = mid - 1
    else:
        left = mid + 1

print(right)