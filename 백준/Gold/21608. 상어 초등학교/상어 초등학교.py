import sys
input = sys.stdin.readline

N = int(input())

classroom = [[0] * N for _ in range(N)]
students = {}

dr = (-1, 0, 0, 1)
dc = (0, -1, 1, 0)

# 빈 칸 하나씩 보면서 4방향 탐색 후, 좋아하는 학생 수, 빈칸 수 계산

for _ in range(N**2):
    student, x1, x2, x3, x4 = map(int, input().split())
    students[student] = (x1, x2, x3, x4)

    candidate = []

    for r in range(N):
        for c in range(N):
            like_student = 0
            blank = 0

            if classroom[r][c] != 0:  # 빈칸 기준만 탐색
                continue

            for z in range(4):
                nr = r + dr[z]
                nc = c + dc[z]

                if not (0 <= nr < N and 0 <= nc < N):
                    continue

                if classroom[nr][nc] in students[student]:
                    like_student += 1
                elif classroom[nr][nc] == 0:
                    blank += 1

            candidate.append((like_student, blank, r, c))

    candidate = sorted(candidate, key= lambda x: (-x[0], -x[1], x[2], x[3]))

    _, _, x, y = candidate[0]

    classroom[x][y] = student

score = 0

for i in range(N):
    for j in range(N):

        number = 0

        for z in range(4):
            nr = i + dr[z]
            nc = j + dc[z]

            if not (0 <= nr < N and 0 <= nc < N):
                continue

            if classroom[nr][nc] in students[classroom[i][j]]:
                number += 1
        
        if number > 0:
            score += 10 ** (number - 1)

sys.stdout.write(str(score))