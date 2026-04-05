import sys
input = sys.stdin.readline

T = int(input())

# 6명 이상이 완주했을 경우 (팀 번호, 합, 5번째 선수 점수) 로 정렬하면 쉽게 구할 수 있을 듯

for _ in range(T):
    N = int(input())
    score_lst = list(map(int, input().split()))

    number_lst = [0] * 201  # 팀 당 선수의 수

    for i in range(N):
        number_lst[score_lst[i]] += 1

    del_team = []
    count_team = []

    for idx, x in enumerate(number_lst[1:]):
        if x == 0:
            continue

        if x != 6:
            del_team.append(idx + 1)
        else:
            count_team.append(idx + 1)

    valid_lst = [[] for _ in range(201)]  # 각 팀 당 유효 점수들

    i, j = 1, 0

    for _ in range(N):
        if not score_lst[j] in del_team:
            valid_lst[score_lst[j]].append(i)
            i += 1
        j += 1

    team_lst = []

    for team in count_team:
        t_lst = valid_lst[team]
        team_lst.append((team, sum(t_lst[:4]), t_lst[4]))

    team_lst.sort(key=lambda lst_: (lst_[1], lst_[2]))

    print(team_lst[0][0])