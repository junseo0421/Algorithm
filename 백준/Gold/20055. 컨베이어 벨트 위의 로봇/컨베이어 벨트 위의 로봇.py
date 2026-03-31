import sys
input = sys.stdin.readline

N, K = map(int, input().split())

a_lst = list(map(int, input().split()))
robot = [0] * N

# 회전 > 이동 (내구도 생각) > 올리기 > 종료

cnt = 1
result = a_lst.count(0)

while True:
    # 벨트 회전 (로봇도 같이 회전)
    robot = [0] + robot[:-2] + [0]
    a_plus = (-cnt) % (2 * N)

    # 로봇 이동 (내구도 닳음)
    for i in range(N-2, -1, -1):
        a_pp = (i + 1 - cnt) % (2 * N)
        if robot[i] == 1 and a_lst[a_pp] != 0 and robot[i + 1] == 0:
            robot[i], robot[i + 1] = 0, 1
            a_lst[a_pp] -= 1

            if a_lst[a_pp] == 0:
                result += 1

    # 로봇 올리기
    if not a_lst[a_plus] == 0:
        if a_lst[a_plus] == 1:
            result += 1
        a_lst[a_plus] -= 1
        robot[0] = 1

    # 종료 조건 및 종료
    if result >= K:
        sys.stdout.write(str(cnt))
        break

    cnt += 1