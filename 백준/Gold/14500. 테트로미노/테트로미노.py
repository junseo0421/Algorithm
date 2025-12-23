import sys
input = sys.stdin.readline

N, M = map(int, input().split())

length = M + 2

paper = [0] * length

for _ in range(N):
    paper += [0] + list(map(int, input().split())) + [0]

paper += [0] * length

visited = [0] * length * (N+2)

ans = 0

def back(n, temp, lst):  # 깊이, 더해질 숫자, index list
    global ans

    if n == 4:
        ans = max(ans, temp)
        return

    for idx in lst:
        for i in (idx+1, idx-1, idx+length, idx-length):
            if visited[i] == 0 and paper[i] != 0:
                visited[i] = 1
                back(n+1, temp+paper[i], lst + [i])
                visited[i] = 0

for r in range(1, N+1):
    for c in range(1, M+1):
        visited[r*length+c] = 1
        back(1, paper[r*length+c], [r*length+c])

sys.stdout.write(str(ans))