import sys
input = sys.stdin.readline

N, M = map(int, input().split())

map_lst = [list(map(int, input().split())) for _ in range(N)]

pos1, pos2 = [], []

for r in range(N):
    for c in range(N):
        if map_lst[r][c] == 1:
            pos1.append((r, c))
        elif map_lst[r][c] == 2:
            pos2.append((r, c))  # index가 밀려도 거리는 같음

dist = [[abs(x2-x1)+abs(y2-y1) for (x2, y2) in pos2] for (x1, y1) in pos1]  # 집에 따른 치킨집들

min_dist = 1e9
check = []

def back(start):
    global min_dist

    # 종료 조건
    if len(check) == M:
        # 거리 계산?
        dist_sum = 0
        for chicken in dist:  # 모든 집 훑기
            house_dist_lst = []
            for idx in check:  # M 개만큼의 index
                house_dist_lst.append(chicken[idx])
            dist_sum += min(house_dist_lst)
        min_dist = min(dist_sum, min_dist)
        return

    # 백트래킹
    for i in range(start, len(pos2)):
        check.append(i)
        back(i+1)
        check.pop()

back(0)
sys.stdout.write(str(min_dist))