import sys
input = sys.stdin.readline

# 최대 점수와 최대 점수를 저장하는 1차원 list 를 따로 두기?

N = int(input())

prev_max = list(map(int, input().split()))

prev_min, max_lst, min_lst = prev_max[:], prev_max[:], prev_max[:]

for _ in range(N-1):
    a, b, c = map(int, input().split())

    max_lst[0] = a + max(prev_max[0], prev_max[1])
    max_lst[1] = b + max(prev_max[0], prev_max[1], prev_max[2])
    max_lst[2] = c + max(prev_max[1], prev_max[2])

    min_lst[0] = a + min(prev_min[0], prev_min[1])
    min_lst[1] = b + min(prev_min[0], prev_min[1], prev_min[2])
    min_lst[2] = c + min(prev_min[1], prev_min[2])

    prev_max, prev_min = max_lst[:], min_lst[:]

sys.stdout.write(str(max(max_lst)) + ' ' + str(min(min_lst)))
