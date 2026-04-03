import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
fireballs = {}

dir_lst = ((0, 2, 4, 6), (1, 3, 5, 7))

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs[(r-1, c-1)] = [(m, s, d)]


def fireball_moving(r, c, s, d):
    r_minus = (r - s) % N
    c_minus = (c - s) % N
    r_plus = (r + s) % N
    c_plus = (c + s) % N

    if d == 0:
        x, y = r_minus, c
    elif d == 1:
        x, y = r_minus, c_plus
    elif d == 2:
        x, y = r, c_plus
    elif d == 3:
        x, y = r_plus, c_plus
    elif d == 4:
        x, y = r_plus, c
    elif d == 5:
        x, y = r_plus, c_minus
    elif d == 6:
        x, y = r, c_minus
    else:
        x, y = r_minus, c_minus

    return x, y


for _ in range(K):
    fireball_over_2 = []
    new_fireballs = {}

    # 파이어볼 방향 d로 속력 s칸 만큼 이동
    for pos in fireballs:
        r, c = pos

        # 한 칸에 여러 파이어볼이 있는 경우도 고려
        for m, s, d in fireballs[pos]:
            n_r, n_c = fireball_moving(r, c, s, d)

            # 이동한 파이어볼을 새로운 dict에 담기
            if not (n_r, n_c) in new_fireballs:
                new_fireballs[(n_r, n_c)] = [(m, s, d)]
            else:
                new_fireballs[(n_r, n_c)].append((m, s, d))
                # 담으면서 2개 이상의 좌표 알아두기
                if (n_r, n_c) not in fireball_over_2:
                    fireball_over_2.append((n_r, n_c))

    # 2개 이상인 칸이 없으면 스킵
    if not fireball_over_2:
        fireballs = new_fireballs
        continue

    # 해당 좌표만 순회하면서 파이어볼 넣어두기
    for pos in fireball_over_2:
        t_m, t_s, cnt = 0, 0, 0
        direction = []

        for m, s, d in new_fireballs[pos]:
            direction.append(d)
            t_m += m
            t_s += s
            cnt += 1

        new_m = t_m // 5

        # 질량이 0이 되면 dict의 key 삭제 후 continue
        if new_m == 0:
            del new_fireballs[pos]
            continue

        new_s = t_s // cnt

        # 합쳐지는 파이어볼 방향 판정
        is_diff = 0

        judge = direction[0] % 2
        for d_ in direction[1:]:
            if judge != d_ % 2:
                is_diff = 1
                break

        final_d = dir_lst[is_diff]

        for i in range(4):
            if i == 0:
                new_fireballs[pos] = [(new_m, new_s, final_d[i])]
            else:
                new_fireballs[pos].append((new_m, new_s, final_d[i]))

    fireballs = new_fireballs

result = 0

for lst in fireballs.values():
    for m, _, _ in lst:
        result += m

sys.stdout.write(str(result))