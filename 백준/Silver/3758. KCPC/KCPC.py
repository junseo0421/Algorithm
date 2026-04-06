import sys
input = sys.stdin.readline

# 순위 우선 순위
# 1. 점수가 높은 팀 / 2. 풀이 제출 횟수 적은 팀 / 3. 마지막 제출 시간이 더 빠른 팀

T = int(input())

for _ in range(T):
    n, k, t, m = map(int, input().split())  # 팀 개수, 문제 개수, 팀 ID, 로그 엔트리 개수

    score_lst = [[0] * k for _ in range(n)]
    submit_num = [0] * n
    last_submit = [0] * n

    for order in range(m):
        i, j, s = map(int, input().split())  # 팀 ID, 문제 번호, 획득 점수
        i -= 1
        j -= 1

        score_lst[i][j] = max(score_lst[i][j], s)
        submit_num[i] += 1
        last_submit[i] = order

    team_lst = [() for _ in range(n)]

    for team in range(n):
        team_lst[team] = (sum(score_lst[team]), submit_num[team], last_submit[team])

    print(sorted(team_lst, key=lambda x:(-x[0], x[1], x[2])).index(team_lst[t-1]) + 1)