import sys
input = sys.stdin.readline

# 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사

# 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능

N = int(input())
towers = list(map(int, input().split()))[::-1]

result = [0] * N
stack = []

for i in range(N):
    if stack:
        while stack[-1][0] <= towers[i]:  # 스택에 있는 수가 다음에 나오는 것보다 작을 때 반복
            h, o = stack.pop()
            result[o] = N - i

            if not stack:
                break

    stack.append((towers[i], i))  # 높이, 순서

print(*result[::-1])
