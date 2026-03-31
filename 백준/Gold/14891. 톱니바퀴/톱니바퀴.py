import sys
input = sys.stdin.readline

from collections import deque


def wheel_rotation(w, r):
    if r == 1:  # 시계 방향
        return w[-1] + w[:-1]
    else:
        return w[1:] + w[0]


def judge(n):
    # 왼쪽 탐색
    for i in range(n, 0, -1):
        if wheel_lst[i][6] != wheel_lst[i-1][2]:
            rot_inform.append(i-1)
        else:
            break

    # 오른쪽 탐색:
    for j in range(n, 3):
        if wheel_lst[j][2] != wheel_lst[j+1][6]:
            rot_inform.append(j+1)
        else:
            break


wheel_lst = []
rot_lst1 = [1, -1, 1, -1]
rot_lst2 = [-1, 1, -1, 1]

for _ in range(4):
    wheel_lst.append(input().rstrip())

K = int(input())
for _ in range(K):
    number, rotation = map(int, input().split())
    number -= 1

    rot_inform = [number]

    if rot_lst1[number] == rotation:
        rot_lst = rot_lst1
    else:
        rot_lst = rot_lst2

    # 돌릴 톱니바퀴 판단
    judge(number)

    # 톱니바퀴 돌리기
    for w in rot_inform:
        wheel_lst[w] = wheel_rotation(wheel_lst[w], rot_lst[w])


result = 0

for w in range(4):
    if wheel_lst[w][0] == '1':
        result += 2 ** w

sys.stdout.write(str(result))