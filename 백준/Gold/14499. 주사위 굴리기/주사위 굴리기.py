import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

# 6자리의 list로 index를 바꿔가며 관리?
dice = [0] * 6

dn = ((), (0, 1), (0, -1), (-1, 0), (1, 0))

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
def rolling(dice, dir):
    new_dice = dice[:]

    if dir == 1:
        new_dice[0], new_dice[2], new_dice[3], new_dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 2:
        new_dice[0], new_dice[2], new_dice[3], new_dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 3:
        new_dice[0], new_dice[1], new_dice[4], new_dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        new_dice[0], new_dice[1], new_dice[4], new_dice[5] = dice[1], dice[5], dice[0], dice[4]

    return new_dice

pos = (x, y)

for c in command:
    # 굴러갈 좌표 구하기
    i = pos[0] + dn[c][0]
    j = pos[1] + dn[c][1]

    # 범위 밖이면 무시, 출력도 X
    if not (0 <= i < N and 0 <= j < M):
        continue

    # 좌표가 허용 범위 안이면 주사위 굴리기
    dice = rolling(dice, c)

    # 좌표가 허용 범위 안이면 대입
    pos = (i, j)

    # 칸이 0인지 아닌지 기준
    # 칸이 0이면 dice[5]를 지도에 복사
    # 칸이 0이 아니면, dice[5]에 복사 후 칸이 0

    if maps[i][j] == 0:
        maps[i][j] = dice[5]
    else:
        dice[5] = maps[i][j]
        maps[i][j] = 0

    sys.stdout.write(str(dice[0]) + '\n')