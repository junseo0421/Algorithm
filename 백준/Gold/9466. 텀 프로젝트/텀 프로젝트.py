import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

T = int(input())


def dfs(n):
    global cycle_total

    visited[n] = True
    nxt = num_lst[n]

    if visited[nxt] == False:
        dfs(nxt)

    # 사이클 확정
    if visited[nxt] == True and finished[nxt] == False:
        cnt = 1
        cur = nxt
        finished[cur] = True

        while True:
            cur = num_lst[cur]

            if cur == nxt:
                break
                
            cnt += 1

        cycle_total += cnt

    finished[n] = True


for _ in range(T):
    n = int(input())
    num_lst = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    finished = [False] * (n + 1)
    cycle_total = 0

    for i in range(1, n + 1):
        if visited[i] == False:
            dfs(i)

    sys.stdout.write(str(n - cycle_total) + '\n')