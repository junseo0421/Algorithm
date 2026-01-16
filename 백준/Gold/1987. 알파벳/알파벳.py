import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = [input().rstrip() for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [False] * 26  # ord('A') = 65

ans = 1

def back(x, y, depth):
    global ans

    ans = max(ans, depth)

    if ans == 26:
        sys.stdout.write(str(ans))
        exit()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < R) and (0 <= ny < C):
            idx = ord(board[nx][ny]) - 65
            if visited[idx] == False:
                visited[idx] = True
                back(nx, ny, depth+1)
                visited[idx] = False

start = ord(board[0][0]) - 65
visited[start] = True
back(0, 0, 1)

sys.stdout.write(str(ans))
