def solution(board):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    length = len(board)
    
    bomb_index = []
    for i in range(length):
        for j in range(length):
            if board[i][j] == 1:
                bomb_index.append((i, j))
                
    for x, y in bomb_index:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < length and 0 <= ny < length:
                board[nx][ny] = 1
                
    count = 0
    for x in range(length):
        for y in range(length):
            if board[x][y] == 0:
                count += 1
            
    return count