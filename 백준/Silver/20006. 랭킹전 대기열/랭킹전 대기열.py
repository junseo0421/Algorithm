import sys
input = sys.stdin.readline

p, m = map(int, input().split())  # 플레이어 수, 방의 정원

room_lst = []

for _ in range(p):
    l, n = input().split()
    l = int(l)

    for i in range(len(room_lst)):
        if len(room_lst[i]) == m:
            continue

        if abs(l - room_lst[i][0][0]) <= 10:
            room_lst[i].append((l, n))
            break

    else:
        room_lst.append([(l, n)])

for lst in room_lst:
    if len(lst) == m:
        print('Started!')
    else:
        print('Waiting!')

    lst = sorted(lst, key=lambda x:x[1])

    for item in lst:
        print(*item)