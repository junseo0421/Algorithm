import sys
input = sys.stdin.readline

from collections import Counter

r, c, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(3)]

# index 맞춰주기
r, c = r-1, c-1

# 빈도수로 정렬하는 방법
# Counter 적용 이후 등장 횟수 오름차순, 수 오름차순로 정렬하면 됨

sec = 0

r_size = 3
c_size = 3

# R 연산: 행에 대해 정렬 / 행 >= 열
# 행 개수만 늘어남
# C 연산: 열에 대해 정렬 / 행 < 열
# 열 개수만 늘어남

while True:
    # 종료 조건 (r, c) 가 lst 밖의 범위일 때도 생각해야함
    if 0 <= r < r_size and 0 <= c < c_size and lst[r][c] == k:
        break

    # R 연산
    if r_size >= c_size:
        r_lst = []
        r_length = {}

        for i in range(r_size):
            r_count = sorted(Counter(lst[i]).items(), key= lambda x: (x[1], x[0]))
            unpacking = [item for tpl in r_count for item in tpl if not tpl[0] == 0]
            r_lst.append(unpacking)
            r_length[i] = len(unpacking)

        max_r = max(r_length.values())

        if max_r > 100:
            max_r = 100

        for i in range(r_size):
            diff_r = max_r - r_length[i]

            if diff_r > 0:
                r_lst[i] += [0] * diff_r
            elif diff_r < 0:
                r_lst[i] = r_lst[i][:100]

        lst = r_lst
        c_size = max_r

    # C 연산
    # 열로 변환한 뒤에, 위와 똑같이 수행하고 다시 반전?
    else:
        c_lst = []
        c_length = {}

        for i in range(c_size):
            c_ = []
            for j in range(r_size):
                c_.append(lst[j][i])


            c_count = sorted(Counter(c_).items(), key= lambda x: (x[1], x[0]))
            unpacking = [item for tpl in c_count for item in tpl if not tpl[0] == 0]
            c_lst.append(unpacking)
            c_length[i] = len(unpacking)

        max_c = max(c_length.values())

        if max_c > 100:
            max_c = 100

        for i in range(c_size):
            diff_c = max_c - c_length[i]

            if diff_c > 0:
                c_lst[i] += [0] * diff_c
            elif diff_c < 0:
                c_lst[i] = c_lst[i][:100]

        final_c = []

        for i in range(max_c):
            c__ = []
            for j in range(c_size):
                c__.append(c_lst[j][i])
            final_c.append(c__)

        lst = final_c
        r_size = max_c

    sec += 1

    if sec > 100:
        sys.stdout.write(str('-1'))
        exit()

sys.stdout.write(str(sec))