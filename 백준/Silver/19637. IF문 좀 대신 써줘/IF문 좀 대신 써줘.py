import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 칭호 개수, 캐릭터 개수
name = []
strength = []

for _ in range(N):
    n, s = input().split()
    name.append(n)
    strength.append(int(s))

for _ in range(M):
    st = int(input())

    left, right = 0, N-1

    while left <= right:
        mid = (right + left) // 2

        if st > strength[mid]:
            left = mid + 1
        else:
            right = mid - 1

    print(name[left])